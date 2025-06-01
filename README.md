# 🎯 Video Accent Classification Pipeline

An end-to-end pipeline for downloading videos, extracting and transcribing audio, generating speaker embeddings, and classifying the speaker’s accent — all wrapped in a user-friendly Streamlit web app.

---

## 🚀 Features

✅ **Download Videos** from YouTube or direct HTTP URLs  
✅ **Extract Audio** from video using `ffmpeg`  
✅ **Transcribe Audio** using OpenAI’s Whisper ASR  
✅ **Generate Speaker Embeddings** with SpeechBrain ECAPA-TDNN  
✅ **Classify Accents** using a pretrained SpeechBrain model  
✅ **Streamlit Web App** for interactive exploration  

---

## 🗂️ Project Structure

```
project_root/
│
├── main.py                  # Entry point for running the pipeline
├── app.py                   # Streamlit web application
├── requirements.txt         # Python dependencies
│
├── utils/                   # Utility functions
│   ├── file_utils.py
│   └── url_utils.py
│
├── downloader/              # Video download modules
│   ├── youtube.py
│   └── http.py
│
├── audio/                   # Audio extraction & preprocessing
│   ├── extractor.py
│   └── preprocess.py
│
├── transcription/           # Whisper-based transcription
│   └── transcriber.py
│
├── speaker/                 # Speaker embedding extraction
│   └── embedder.py
│
└── accent/                  # Accent classification
    └── classifier.py
```

---

## ⚙️ Installation

1. **Clone the repository**

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

## 🧪 Usage

### 🔧 Run from Command Line

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

### 🌐 Run Streamlit Web App

```bash
streamlit run app.py
```

Then open your browser to the provided localhost URL, enter a video URL, and view results interactively.

---

## 📌 Notes

- Uses **Whisper base** model on **CPU** by default  
- Speaker embedding via **SpeechBrain ECAPA-TDNN**  
- Accent classifier from **SpeechBrain pretrained models**  
- Audio expected in **16kHz mono WAV** format  
- First-time model downloads require an **active internet connection**  

---

## 📝 License

**MIT License**

---

## 🙏 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper)  
- [SpeechBrain](https://speechbrain.readthedocs.io/)  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
- [FFmpeg](https://ffmpeg.org/)  
- [Streamlit](https://streamlit.io/)  
