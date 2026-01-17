import os
from pathlib import Path

from config import Config as BaseConfig


class YTMusicDLConfig(BaseConfig):
    """Configuration for ytmusic_dl."""

    # Default paths (WSL paths for E: drive)
    DEFAULT_DOWNLOAD_DIR = Path(os.getenv("YTMUSIC_DL_DOWNLOAD_DIR", "/mnt/e/jerry/Music"))
    DEFAULT_HISTORY_FILE = Path(
        os.getenv(
            "YTMUSIC_DL_HISTORY_FILE",
            "/mnt/e/jerry/Documents/PythonScripts/yt-dlp_related/ytmusic_downloaded.jsonl",
        )
    )
