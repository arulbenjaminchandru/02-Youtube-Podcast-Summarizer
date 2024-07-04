import streamlit as st
import re
import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
import pysbd
import dotenv
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models import ModelInference


dotenv.load_dotenv()

def configure_watsonx():
# Configure WatsonX Mistral AI Model
    credentials = {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey": os.getenv("WATSONX_API_KEY")
    }
    project_id = os.getenv("PROJECT_ID")
    print([model.name for model in ModelTypes])

    model_id = "mistralai/mixtral-8x7b-instruct-v01"

    parameters = {
        GenParams.DECODING_METHOD: "greedy",
        GenParams.MIN_NEW_TOKENS: 1,
        GenParams.MAX_NEW_TOKENS: 150
    }

    model = ModelInference(
        model_id=model_id, 
        params=parameters, 
        credentials=credentials,
        project_id=project_id)
    
    return model


seg = pysbd.Segmenter(language='en', clean=True)

def extract_youtube_video_id(url: str) -> str:
    found = re.search(r"(?:youtu\.be\/|watch\?v=)([\w-]+)", url)
    if found:
        return found.group(1)
    return None

def get_video_transcript(video_id: str) -> str | None:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except TranscriptsDisabled:
        return None
    return ' '.join([line["text"] for line in transcript])

def chunk_large_text(text_list: list, max_size: int) -> list[str]:
    txts = []
    para = ''
    for s in text_list:
        s_len = len(s)
        if para and len(para) + s_len > max_size:
            txts.append(para)
            para = ''
        if s_len <= max_size:
            para += s + '\n'
        else:
            if para:
                txts.append(para)
                para = ''
            cut = s_len // max_size
            chunk = s_len // (cut + 1)
            i = 0
            while i < s_len:
                if s_len - i <= chunk:
                    txts.append('… ' + s[i:] + ' …')
                    break
                clip_i = s.find(' ', i + chunk)
                txts.append('… ' + s[i:clip_i] + ' …')
                i = clip_i + 1
    if para:
        txts.append(para)
    return txts

def summarize_large_text(text_list: list, max_size: int) -> str:
    summaries = ""
    txts = chunk_large_text(text_list, max_size)
    summaries = summaries.join(txts)
    return summaries

# Streamlit UI
st.title('YouTube Transcript Summarizer using watsonx Mistral 7B')
url = st.text_input('Enter YouTube URL')
submit = st.button('Submit')

if submit and url:
    video_id = extract_youtube_video_id(url)
    if video_id:
        transcript = get_video_transcript(video_id)
        if transcript:
            text_list = seg.segment(transcript)
            summary = summarize_large_text(text_list, max_size=2048)
            st.subheader("Extracted Text from Video")
            st.write(summary)
            if summary:
                model = configure_watsonx()
                prompt = "Summarize the following content within 150 tokens : "
                summary = prompt + "\n" + summary
                response = model.generate(summary)
                st.subheader('Summary')
                st.write(response.get('results')[0]['generated_text'])
        else:
            st.write("No transcript found for this video.")
    else:
        st.write("Invalid YouTube URL.")
