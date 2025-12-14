# Useful Tools

This repository contains a collection of command-line utilities.

## Getting Started

Follow these steps to set up the project environment before using any specific utility.

### 1. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

You can create and activate one easily with `uv`:

```bash
# This command creates and activates a virtual environment in .venv
uv venv
```

Alternatively, you can use Python's standard `venv` module:

```bash
# Create the virtual environment
python -m venv .venv

# Activate it (Linux/macOS)
source .venv/bin/activate

# Activate it (Windows PowerShell)
# .\.venv\Scripts\Activate.ps1
```

### 2. Configure Environment Variables

The project uses a `.env` file for configuration (e.g., log levels). Copy the example file to create your own local configuration:

```bash
cp .env.example .env
```

You can then edit the `.env` file to customize settings.

### 3. Install the Base Project

Install the core project structure in editable mode. This step does not install dependencies for any specific utility, but makes the project's packages available to your environment.

```bash
uv pip install -e .
```

> [!NOTE]
> To install the dependencies for all available utilities at once, you can use the `[all]` extra:
> `uv pip install -e '.[all]'`


## Available Utilities

### Chinese Converter

A flexible, multi-format tool for converting Chinese text between Simplified and Traditional characters.

**Features:**

-   Supports `.epub` and `.txt` files.
-   Multiple conversion profiles (e.g., Simplified to Traditional, Traditional to Simplified).
-   Batch processing for directories.
-   Automatic backup creation.

**Installation:**

To use the Chinese Converter, install its specific dependencies using the `[chinese_converter]` extra:

```bash
uv pip install -e .'[chinese_converter]'
```

**Usage:**

The script can be run as a module from the project root:

```bash
python -m chinese_converter <input> [output] [options]
```

**Arguments:**

| Argument          | Description                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| `input`           | The source file (`.epub`, `.txt`) or directory to convert.                                                  |
| `output`          | (Optional) The destination file or directory. If omitted, a default name will be generated (e.g., `_trad` suffix). |
| `-t`, `--type`    | (Optional) The conversion type. Defaults to `s2t`.<br>Options: `s2t`, `s2tw`, `s2hk`, `t2s`.                  |
| `-b`, `--batch`   | (Optional) Treat the input as a directory for batch processing.                                             |
| `--no-backup`     | (Optional) Disable the creation of a backup file for single-file conversions.                               |

**Examples:**

1.  **Convert a single EPUB file:**
    This will create `my_book_trad.epub` in the same directory.
    ```bash
    python -m chinese_converter "path/to/my_book.epub"
    ```

2.  **Convert a single TXT file from Traditional to Simplified:**
    ```bash
    python -m chinese_converter "path/to/my_document.txt" --type t2s
    ```

3.  **Convert a directory of files:**
    This converts all `.epub` and `.txt` files from `books_simplified` and saves them in `books_traditional`.
    ```bash
    python -m chinese_converter "path/to/books_simplified" "path/to/books_traditional" --batch
    ```

---

### Anime1 Downloader

A command-line tool to download videos from anime1.me.

**Features:**

-   Download single episodes or entire series.
-   Multi-threaded downloading for faster performance.
-   Bypass Cloudflare protection with cookies.
-   Extract video URLs without downloading.

**Installation:**

To use the Anime1 Downloader, install its specific dependencies using the `[anime1_downloader]` extra:

```bash
uv pip install -e .'[anime1_downloader]'
```

**Usage:**

The script can be run as a module from the project root:

```bash
python -m anime1_downloader <url> [options]
```

**Arguments:**

| Argument                       | Description                                                                                                                            |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| `url`                          | A direct URL to an anime1.me page (e.g., `https://anime1.me/18305`). You may need to wrap this in quotes.                                  |
| `-x`, `--extract`              | Only extract URLs, do not download.                                                                                                    |
| `-cf`, `--cloudflare`          | Set cf_clearance cookie to bypass Cloudflare detection. This cookie is valid for one hour. You may need to wrap this in quotes.         |
| `-ua`, `--user-agent`          | Set user-agent to bypass detection.                                                                                                    |
| `-o`, `--output-dir`           | Set the base output directory for downloaded videos. Final path will be `<DIR>/<anime_series_name>/`. Defaults to the value in your `.env` file. |
| `-j`, `--max-concurrent-downloads` | Maximum number of concurrent video downloads. Defaults to the value in your `.env` file.                                               |

**Example:**

```bash
python -m anime1_downloader "https://anime1.me/18305" -j 8
```

---

### Image Tool

A multi-functional tool for image and video manipulation.

**Features:**

-   **Coordinate Marking**: View an image, mark coordinates with mouse clicks, and save the marked image.
-   **Frame Extraction**: Extract a specific frame from a video file.
-   **Image Capture**: Capture images from a camera.

**Installation:**

To use the Image Tool, install its specific dependencies using the `[image_tool]` extra:

```bash
uv pip install -e .'[image_tool]'
```

**Usage:**

The script can be run as a module from the project root with the following subcommands:

```bash
python -m image_tool <subcommand> [options]
```

#### `coords`

View an image and mark coordinates.

**Arguments:**

| Argument          | Description                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| `image_path`      | Path to the image file.                                                                                     |
| `--ratio`         | (Optional) The resize ratio for the image.                                                                  |

**Example:**

```bash
python -m image_tool coords "path/to/my_image.jpg" --ratio 0.5
```

#### `frame`

Extract a frame from a video.

**Arguments:**

| Argument          | Description                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| `-v`, `--video`   | Path to the input video file.                                                                               |
| `-t`, `--time`    | Time in seconds at which to extract the frame.                                                              |
| `-o`, `--output`  | (Optional) Directory to save the extracted frame.                                                           |

**Example:**

```bash
python -m image_tool frame -v "path/to/my_video.mp4" -t 60 -o "path/to/output"
```

#### `capture`

Capture an image from a camera.

**Arguments:**

| Argument          | Description                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| `-c`, `--camera`  | (Optional) The camera index to use.                                                                         |
| `-s`, `--save_dir`| (Optional) Directory to save the captured images.                                                           |

**Example:**

```bash
python -m image_tool capture -c 1 -s "path/to/captures"
```
---

### YouTube Music Downloader

A tool to download audio from YouTube videos/playlists and manage your local music library.

**Features:**

-   **Download**: Download audio from YouTube videos, playlists, or channels.
-   **Verify**: Check your local backup against a history file to find missing songs.
-   **Metadata**: Extract YouTube IDs from downloaded files.
-   **Migrate**: Redownload songs from a text list.

**Installation:**

To use the YouTube Music Downloader, install its specific dependencies using the `[ytmusic_dl]` extra:

```bash
uv pip install -e .'[ytmusic_dl]'
```

**Usage:**

The script can be run as a module from the project root:

```bash
python -m ytmusic_dl <command> [options]
```

#### `download`

Download audio from YouTube.

**Arguments:**

| Argument          | Description                                                                 |
| ----------------- | --------------------------------------------------------------------------- |
| `urls`            | One or more YouTube URLs (video/playlist/channel).                          |
| `-o`, `--output`  | Output directory. Defaults to configured path.                              |
| `-f`, `--format`  | Audio format (e.g., `mp3`). Default is `best` (keeps original).             |
| `-dr`, `--dry-run`| Show what would be downloaded without downloading.                          |

**Example:**

```bash
python -m ytmusic_dl download "https://music.youtube.com/playlist?list=..."
```

#### `verify`

Verify backup files against history.

**Arguments:**

| Argument          | Description                                                                 |
| ----------------- | --------------------------------------------------------------------------- |
| `-b`, `--backup-dir` | Directory containing the backup audio files.                             |
| `-d`, `--download-missing` | Automatically download missing songs.                                |

**Example:**

```bash
python -m ytmusic_dl verify -d
```
