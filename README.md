# YouTube Transcript Summarizer built with Streamlit and IBM WatsonX Mistral AI Model

This project is a YouTube Transcript Summarizer built with Streamlit and IBM WatsonX Mistral AI Model. The application extracts the transcript from a given YouTube video URL, chunks the transcript into manageable pieces, and generates a concise summary.

## Prerequisites

- Python 3.6 or later
- IBM WatsonX API credentials

## Installation

0. Get watsonX API credentials

   We need an API Key and project ID to access the models present in watsonX. To get that, please follow below instructions,

   Get a WML API key from https://cloud.ibm.com/iam/apikeys

    Create a watsonX project in https://dataplatform.cloud.ibm.com/wx/home and associate it with WML service on cloud (Watson Machine Learning). Also get the project id of this project.

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/youtube-transcript-summarizer.git
    cd youtube-transcript-summarizer
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required libraries:
    ```bash
    pip install streamlit re youtube_transcript_api pysbd python-dotenv ibm-watsonx
    ```

4. Create a `.env` file in the project directory and add your WatsonX API key and project ID:
    ```env
    WATSONX_API_KEY=your_watsonx_api_key
    PROJECT_ID=your_project_id
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the YouTube URL of the video you want to summarize and click "Submit".

## Project Structure

- `app.py`: The main application file containing the Streamlit UI and logic for summarizing YouTube transcripts.
- `.env`: Environment file containing API credentials (not included in the repository, must be created by the user).

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.
