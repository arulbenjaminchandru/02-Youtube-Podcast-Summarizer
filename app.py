import streamlit as st
import re
import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
import pysbd
import dotenv
import google.generativeai as genai


dotenv.load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

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
    txts = chunk_large_text(text_list, max_size)
    prompt = "Summarize the following content"
    summaries = prompt.join(txts)
    response = model.generate_content(summaries)
    print(response.text)
    return response.text

# Streamlit UI
st.title('YouTube Transcript Summarizer')
url = st.text_input('Enter YouTube URL')
submit = st.button('Submit')

if submit and url:
    video_id = extract_youtube_video_id(url)
    if video_id:
        transcript = get_video_transcript(video_id)
        if transcript:
            text_list = seg.segment(transcript)
            summary = summarize_large_text(text_list, max_size=2048)
            st.subheader('Summary')
            st.write(summary)
        else:
            st.write("No transcript found for this video.")
    else:
        st.write("Invalid YouTube URL.")
