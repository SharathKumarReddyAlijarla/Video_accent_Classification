import streamlit as st
from utils.url_utils import is_url, is_youtube_url
from downloader.youtube import download_video_youtube
from downloader.http import download_video_http
from audio.extractor import extract_audio
from audio.preprocess import preprocess_audio
from transcription.transcriber import transcribe_audio
from accent.classifier import classify_accent


def main():
    st.title("Video Accent Classification Pipeline")

    video_url = st.text_input("Enter YouTube or direct video URL:")

    if st.button("Process Video"):
        if not video_url:
            st.error("Please enter a video URL.")
            return

        if not is_url(video_url):
            st.error("Invalid URL format.")
            return

        st.info("Starting the pipeline...")

        # Download video
        if is_youtube_url(video_url):
            st.info("Downloading video from YouTube...")
            video_path = download_video_youtube(video_url)
        else:
            st.info("Downloading video from direct URL...")
            video_path = download_video_http(video_url)

        st.success(f"Video downloaded: {video_path}")

        # Extract audio
        st.info("Extracting audio from video...")
        audio_path = extract_audio(video_path)
        st.success(f"Audio extracted: {audio_path}")

        # Preprocess audio
        st.info("Preprocessing audio for accent classification...")
        processed_audio = preprocess_audio(audio_path)
        st.success(f"Audio preprocessed: {processed_audio}")

        # Transcribe audio
        st.info("Transcribing audio...")
        transcription_result = transcribe_audio(processed_audio)
        st.success("Transcription completed!")

        st.subheader("Transcription Output")
        st.write(transcription_result)

        # Classify accent
        st.info("Classifying accent...")
        accent, index, confidence, _ = classify_accent(processed_audio)
        st.success("Accent classification completed!")

        st.subheader("Accent Classification Result")
        st.write(f"Predicted Accent: {accent}")
        st.write(f"Confidence Score: {confidence:.2f}%")


if __name__ == "__main__":
    main()
