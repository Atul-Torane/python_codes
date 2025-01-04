# module.py
import argparse
from logger import app_logger

def parse_arguments():
    parser = argparse.ArgumentParser(description="Argument parsing module")

    # Add arguments with default values
    parser.add_argument('--name', type=str, help='Your name', default='Unknown')
    parser.add_argument('--age', type=int, help='Your age', default=00)

    # Log the parsed arguments
    app_logger.debug("Parsing arguments.")
    args = parser.parse_args()

    return args
