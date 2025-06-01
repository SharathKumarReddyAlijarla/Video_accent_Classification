import os
from pathlib import Path


def create_file_structure(
    root_dir=r"D:\Data Science Projects\Video_accent_Classification",
):
    """Creates the specified file structure for the project."""

    # Define the directory structure
    structure = {
        "main.py": "# Entry point to run the pipeline\n",
        "requirements.txt": "# Project dependencies\n",
        "utils/__init__.py": "",
        "utils/file_utils.py": '# File utility functions\n"""\nFunctions:\n- remove_if_exists\n- get_filename_from_url\n"""\n',
        "utils/url_utils.py": '# URL utility functions\n"""\nFunctions:\n- is_url\n- is_youtube_url\n"""\n',
        "downloader/__init__.py": "",
        "downloader/youtube.py": '# YouTube video downloader\n"""\nFunction:\n- download_video_youtube\n"""\n',
        "downloader/http.py": '# HTTP video downloader\n"""\nFunction:\n- download_video_http\n"""\n',
        "audio/__init__.py": "",
        "audio/extractor.py": '# Audio extraction from video\n"""\nFunction:\n- extract_audio\n"""\n',
        "audio/preprocess.py": '# Audio preprocessing for accent classification\n"""\nFunction:\n- preprocess_audio\n"""\n',
        "transcription/__init__.py": "",
        "transcription/transcriber.py": '# Whisper transcription logic\n"""\nFunction:\n- transcribe_audio\n"""\n',
        "speaker/__init__.py": "",
        "speaker/embedder.py": '# Speaker embedding extraction\n"""\nFunction:\n- get_speaker_embedding\n"""\n',
        "accent/__init__.py": "",
        "accent/classifier.py": '# Accent classification\n"""\nFunction:\n- classify_accent\n"""\n',
    }

    # Create the directory structure and files
    for path, content in structure.items():
        full_path = Path(root_dir) / path
        os.makedirs(full_path.parent, exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Created: {full_path}")

    print(f"\nProject structure created successfully in '{root_dir}'")


if __name__ == "__main__":
    create_file_structure()
