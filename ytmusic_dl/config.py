from pathlib import Path

from config import Config as BaseConfig


class YTMusicDLConfig(BaseConfig):
    """Configuration for ytmusic_dl."""

    # Default paths (WSL paths for E: drive)
    DEFAULT_DOWNLOAD_DIR = Path("/mnt/e/jerry/Music")
    DEFAULT_HISTORY_FILE = Path(
        "/mnt/e/jerry/Documents/PythonScripts/yt-dlp_related/ytmusic_downloaded.jsonl"
    )
