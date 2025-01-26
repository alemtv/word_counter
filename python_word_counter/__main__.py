import argparse
import logging
import time
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--directory",
        type=str,
        required=True,
        help="Path to the directory containing .txt files",
    )
    return parser.parse_args()

def count_words_in_file(file_path: str) -> int:
    try:
        with Path.open(file_path, encoding="utf-8") as file:
            content = file.read()
        words = content.split()
        return len(words)
    except FileNotFoundError:
        logging.exception("File not found")
        raise
    except Exception:
        logging.exception("Error processing file %s", file_path)
        raise

def read_all_txt_files(directory: Path) -> None:
    if not directory.is_dir():
        logging.error("The provided path %s is not a directory.", directory)
        return

    for txt_file in directory.glob("*.txt"):
        logging.info("Reading file: %s", txt_file.name)
        try:
            word_count = count_words_in_file(txt_file)
        except Exception:
            logging.exception("An error occurred")
            break
        logging.info("Word count: %s", word_count)

def main() -> None:
    start_time = time.time()
    args = parse_arguments()
    directory_path = Path(args.directory)
    read_all_txt_files(directory_path)
    processing_time = time.time() - start_time
    logging.info("Files processed in %s seconds.", processing_time)

if __name__ == "__main__":
    main()
