# YouTube video downloader
"""
Function:
- download_video_youtube
"""
# downloader/youtube.py

import yt_dlp
from utils.file_utils import remove_if_exists, get_filename_from_url


def download_video_youtube(youtube_url, output_path=None):
    """
    Downloads a YouTube video using yt_dlp.
    """
    if output_path is None:
        output_path = get_filename_from_url(youtube_url, "yt_video", "mp4")

    remove_if_exists(output_path)
    print("[~] Detected YouTube URL. Downloading with yt-dlp...")

    ydl_opts = {
        "format": "mp4",
        "outtmpl": output_path,
        "quiet": False,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    print(f"[✓] Downloaded YouTube video to {output_path}")
    return output_path
