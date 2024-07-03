Sure! Here’s a README file for your project:

---

# YouTube Transcript Summarizer

This project is a web application that takes a YouTube URL, fetches the transcript of the video, and summarizes it using Gemini AI. The web interface is built using Streamlit.

## Features

- Extracts transcript from YouTube videos.
- Summarizes the transcript using Gemini AI.
- Simple and intuitive web interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/YouTubeTranscriptSummarizer.git
    cd YouTubeTranscriptSummarizer
    ```

2. **Install the required packages**:

    ```bash
    pip install streamlit youtube-transcript-api pysbd requests dotenv
    ```

3. **Set up environment variables**:

    Create a `.env` file in the root directory and add your Gemini AI API key:

    ```plaintext
    GEMINI_API_KEY=your_gemini_api_key
    ```

## Usage

1. **Run the Streamlit application**:

    ```bash
    streamlit run app.py
    ```

2. **Open your web browser**:

    Visit `http://localhost:8501` to access the application.

3. **Input YouTube URL**:

    Enter the URL of the YouTube video you want to summarize and click the "Submit" button. The application will fetch the transcript, summarize it, and display the summary.

## File Structure

```
.
├── app.py              # Main application file
├── README.md           # This README file
└── .env                # Environment variables file (to be created)
```

## Dependencies

- **Streamlit**: Web app framework for creating custom web applications.
- **youtube-transcript-api**: Library to fetch YouTube video transcripts.
- **pysbd**: Rule-based sentence boundary detection library.
- **requests**: Simple HTTP library for Python.
- **dotenv**: Library to load environment variables from a `.env` file.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

Arul Benjamin Chandru E - [arulbenjaminchandru@gmail.com](mailto:arulbenjaminchandru@gmail.com)

Project Link: [https://github.com/arulbenjaminchandru/02-Youtube-Podcast-Summarizer/](https://github.com/arulbenjaminchandru/02-Youtube-Podcast-Summarizer/)
