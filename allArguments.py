# allArguments.py
import argparse

def parse_arguments():
    """Function to parse command-line arguments"""
    parser = argparse.ArgumentParser(description="Argument parsing module")

    # Add arguments
    parser.add_argument('--name', type=str, help='Your name', required=True)
    parser.add_argument('--age', type=int, help='Your age', required=True)

    # Parse and return arguments
    return parser.parse_args()
