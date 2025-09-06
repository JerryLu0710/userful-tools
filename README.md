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

---

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