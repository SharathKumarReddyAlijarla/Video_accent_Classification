# Entry point to run the pipeline
from utils.file_utils import remove_if_exists, get_filename_from_url
from utils.url_utils import is_url, is_youtube_url
from downloader.youtube import download_video_youtube
from downloader.http import download_video_http
from audio.extractor import extract_audio
from audio.preprocess import preprocess_audio
from transcription.transcriber import transcribe_audio
from speaker.embedder import get_speaker_embedding
from accent.classifier import classify_accent


def handle_video_input(input_path_or_url):
    if is_url(input_path_or_url):
        if is_youtube_url(input_path_or_url):
            video_path = download_video_youtube(input_path_or_url)
        else:
            video_path = download_video_http(input_path_or_url)
    else:
        print("[~] Detected local video file.")
        video_path = input_path_or_url

    return video_path


def main(input_path_or_url):
    print("\n=== Starting pipeline ===\n")

    # Step 1: Download video or accept local path
    video_path = handle_video_input(input_path_or_url)
    print(f"Video ready at: {video_path}")

    # Step 2: Extract audio from video
    audio_path = extract_audio(video_path)
    print(f"Audio extracted at: {audio_path}")

    # Step 3: Transcribe audio using Whisper
    transcription = transcribe_audio(audio_path)
    print(f"\n--- Transcription ---\n{transcription}\n")

    # Step 4: Get speaker embedding vector
    embedding_vector = get_speaker_embedding(audio_path)
    print(f"Speaker embedding vector shape: {embedding_vector.shape}")

    # Step 5: Preprocess audio for accent classification
    processed_audio_path = preprocess_audio(audio_path)

    # Step 6: Classify accent
    accent, index, confidence, _ = classify_accent(processed_audio_path)
    print(f"Predicted Accent: {accent}")
    print(f"Confidence Score: {confidence:.2f}%")

    print("\n=== Pipeline finished ===\n")

    # Optionally return data
    return {
        "video_path": video_path,
        "audio_path": audio_path,
        "transcription": transcription,
        "speaker_embedding": embedding_vector,
        "accent": accent,
        "accent_confidence": confidence,
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python main.py <video_path_or_url>")
        sys.exit(1)

    input_path_or_url = sys.argv[1]
    results = main(input_path_or_url)
