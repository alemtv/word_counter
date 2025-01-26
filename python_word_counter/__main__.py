import argparse
import time
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "directory",
        type=str,
        help="Path to the directory containing .txt files"
    )
    return parser.parse_args()

def count_words_in_file(file_path: str) -> int:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        words = content.split()
        return len(words)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
        raise

def read_all_txt_files(directory: Path) -> None:
    if not directory.is_dir():
        logging.error(f"The provided path '{directory}' is not a directory.")
        return

    for txt_file in directory.glob("*.txt"):
        logging.info(f"Reading file: {txt_file.name}")
        try:
            word_count = count_words_in_file(txt_file)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            break
        logging.info(f"Word count: {word_count}")

def main() -> None:
    start_time = time.time()
    args = parse_arguments()
    directory_path = Path(args.directory)
    read_all_txt_files(directory_path)
    processing_time = time.time() - start_time
    logging.info(f"Files processed in {processing_time:.5f} seconds.")

if __name__ == "__main__":
    main()
