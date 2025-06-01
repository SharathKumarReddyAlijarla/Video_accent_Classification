# Audio extraction from video
"""
Function:
- extract_audio
"""
# audio/extractor.py

import shutil
import subprocess
from utils.file_utils import remove_if_exists


def extract_audio(video_path, audio_path="extracted_audio.wav", max_duration=None):
    """
    Extracts audio from a video file using ffmpeg.
    The output is a mono, 16kHz, 16-bit PCM WAV file.
    """
    remove_if_exists(audio_path)

    if not shutil.which("ffmpeg"):
        raise EnvironmentError(
            "ffmpeg not found. Please install it and ensure it's in your PATH."
        )

    command = [
        "ffmpeg",
        "-y",
        "-i",
        video_path,
        "-vn",
        "-acodec",
        "pcm_s16le",
        "-ar",
        "16000",
        "-ac",
        "1",
    ]

    if max_duration:
        command.extend(["-t", str(max_duration)])

    command.append(audio_path)

    print(f"[~] Extracting audio from: {video_path}")
    subprocess.run(command, check=True)
    print(f"[✓] Extracted audio to {audio_path}")

    return audio_path
