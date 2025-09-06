"""
Multi-format Chinese Text Converter Module

Converts simplified Chinese text to traditional Chinese (or vice versa) in various file formats.
"""

__version__ = "1.0.0"
__author__ = "Jerry"

from .cli import ChineseTextConverter
from .text_converter import ChineseConverter
from .formats.epub_handler import EPUBHandler
from .formats.txt_handler import TXTHandler

__all__ = ["ChineseTextConverter", "ChineseConverter", "EPUBHandler", "TXTHandler"]
