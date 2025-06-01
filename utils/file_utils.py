# File utility functions
"""
Functions:
- remove_if_exists
- get_filename_from_url
"""
# utils/file_utils.py

import os
import hashlib


def remove_if_exists(filepath):
    """Deletes the file if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)


def get_filename_from_url(url, prefix, ext):
    """Generates a hashed filename from a URL."""
    url_hash = hashlib.md5(url.encode()).hexdigest()
    return f"{prefix}_{url_hash}.{ext}"
