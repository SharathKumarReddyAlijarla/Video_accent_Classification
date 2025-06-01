# HTTP video downloader
"""
Function:
- download_video_http
"""
# downloader/http.py

import requests
from utils.file_utils import remove_if_exists, get_filename_from_url


def download_video_http(video_url, output_path=None):
    """
    Downloads a video from a direct HTTP URL.
    """
    if output_path is None:
        output_path = get_filename_from_url(video_url, "http_video", "mp4")

    remove_if_exists(output_path)
    print("[~] Detected direct video URL. Downloading with requests...")

    response = requests.get(video_url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Failed to download video: {video_url}")

    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)

    print(f"[✓] Downloaded video to {output_path}")
    return output_path
