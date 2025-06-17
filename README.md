#  Video Accent Classification Pipeline

An end-to-end pipeline for downloading videos, extracting and transcribing audio, generating speaker embeddings, and classifying the speaker’s accent — all wrapped in a user-friendly Streamlit web app.

---

##  Features

 **⚪Download Videos** from YouTube or HTTP URLs  
 **⚫Extract Audio** from video using `ffmpeg`  
 **⚪Transcribe Audio** using OpenAI’s Whisper ASR  
 **⚫Generate Speaker Embeddings** with SpeechBrain ECAPA-TDNN  
 **⚪Classify Accents** using a pretrained SpeechBrain model  
 **⚫Streamlit Web App** for interactive exploration  

---


## 🗂️ Project Structure

```
project_root/
│
├── main.py # Core pipeline runner
├── app.py # Streamlit web interface
├── requirements.txt # Dependencies
├── create_file_structure.py # Initializes necessary directories
│
├── utils/ # Utility functions
│ └── helpers.py
│
├── downloader/ # Downloads videos from URL
│ └── downloader.py
│
├── audio/ # Audio extraction/preprocessing
│ ├── audio_extractor.py
│ └── audio_preprocessor.py
│
├── transcription/ # Whisper-based ASR transcription
│ └── transcriber.py
│
├── speaker/ # Speaker embedding logic
│ └── embedder.py
│
├── accent/ # Accent classification module
│ └── classifier.py
│
├── My_Loom_Sample.mp4 # Example video
├── README.md # This documentation file
└── research.ipynb # Research/experimentation notebook```
```

---

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone <repo-url>
cd <repo-folder>
```


2. **Create and activate a virtual environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```


3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Ensure `ffmpeg` is installed** and accessible in your system PATH  
   🔗 [Download FFmpeg](https://ffmpeg.org/download.html)

---

##  Usage

###  Run from Command Line

```bash
python main.py "<video_url_or_local_path>"
```

**Example:**

```bash
python main.py "https://youtu.be/nIwU-9ZTTJc?si=Ba6XvQSEv8nwEBGH"
```

📌 This will:
- Download the video (if URL)
- Extract audio
- Transcribe speech using Whisper
- Generate speaker embedding
- Classify accent using pretrained model
- Print results and save transcription to file

###  Run Streamlit Web App

```bash
streamlit run app.py
```

Then open your browser to the provided localhost URL, enter a video URL, and view results interactively.

---

## Results

Streamlit and CLI will output results like:

| Video Link                                     | Video Description | Predicted Accent | True Accent | Confidence |
|------------------------------------------------|-------------------|------------------|-------------|------------|
| [https://youtu.be/example1   ](https://youtu.be/nIwU-9ZTTJc?si=v07_s4B4-o4zFB4U)                   | Emma Watson speech from Youtube   | England          | England        | 78.87       |
| [https://storage.googleapis.com/sample2.mp4 ](https://github.com/SharathKumarReddyAlijarla/Video_accent_Classification/blob/main/My_Loom_Sample.mp4)    | My loom video sample    | Indian           | Indian      | 55      |


##  Model & Frameworks Used

| Component      | Framework       | Description                                      |
|----------------|------------------|--------------------------------------------------|
| Transcription  | OpenAI Whisper   | Automatic speech recognition (ASR)              |
| Embedding      | SpeechBrain      | ECAPA-TDNN model for speaker representation     |
| Classifier     | SpeechBrain      | Pretrained X-vector accent classifier           |
| Downloader     | yt-dlp           | Efficient YouTube & video downloading           |
| Web App        | Streamlit        | Simple browser-based UI                         |
  


---

## Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)  
- [SpeechBrain](https://speechbrain.readthedocs.io/)  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
- [FFmpeg](https://ffmpeg.org/)  
- [Streamlit](https://streamlit.io/)  
