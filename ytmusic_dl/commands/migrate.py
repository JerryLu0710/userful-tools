import os
import subprocess
import sys

from ytmusic_dl.common.logger import logger


def migrate_command(args):
    """
    Reads video IDs from a text file and redownloads them efficiently
    by passing all IDs to the download command.
    """
    downloaded_txt_path = args.file_path

    if not downloaded_txt_path.exists():
        logger.error(f"Error: '{downloaded_txt_path}' not found.")
        sys.exit(1)

    with open(downloaded_txt_path, encoding="utf-8") as f:
        lines = f.readlines()

    video_ids = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        # Expecting format: "youtube <id>" or just "<id>" if we want to be flexible,
        # but original script enforced "youtube <id>".
        if len(parts) != 2 or parts[0] != "youtube":
            logger.warning(f"Skipping invalid line: {line}")
            continue

        video_ids.append(parts[1])

    if not video_ids:
        logger.warning("No valid video IDs found to download.")
        sys.exit(0)

    logger.info(f"Found {len(video_ids)} songs to redownload. Starting batch process...")

    # Construct command to call the CLI itself
    command = [
        sys.executable,
        "-m",
        "ytmusic_dl.cli",
        "download",
        "--log-level",
        "INFO",
        "--",  # This tells argparse to treat subsequent args as positional
        *video_ids,  # Unpack all video IDs as arguments
    ]

    process_env = os.environ.copy()
    process_env["PYTHONUTF8"] = "1"

    try:
        # Run the command once with all IDs.
        # We use Popen to stream output in real-time.
        with subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            env=process_env,
        ) as process:
            if process.stdout:
                for line in iter(process.stdout.readline, ""):
                    print(line, end="")

            return_code = process.wait()
            if return_code != 0:
                logger.error(f"Download process failed with return code: {return_code}")

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

    logger.info("All songs have been processed.")
