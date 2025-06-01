# URL utility functions
"""
Functions:
- is_url
- is_youtube_url
"""
# utils/url_utils.py


def is_url(path):
    """Returns True if the path is a URL."""
    return path.startswith("http://") or path.startswith("https://")


def is_youtube_url(url):
    """Returns True if the URL is a YouTube link."""
    return "youtube.com" in url or "youtu.be" in url
