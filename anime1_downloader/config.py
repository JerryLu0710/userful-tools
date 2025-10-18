"""Anime1 downloader specific configuration."""
import os
from dotenv import load_dotenv

load_dotenv()


class AnimeDownloaderConfig:
    """Anime1 downloader specific configuration."""

    DOWNLOAD_DIR = os.getenv("ANIME1_DOWNLOAD_DIR", "anime")
    MAX_CONCURRENT_DOWNLOADS = int(os.getenv("ANIME1_MAX_CONCURRENT_DOWNLOADS", 4))
