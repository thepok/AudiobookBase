#!/usr/bin/env python3
"""Simple utility for converting text files to speech."""

import argparse
from pathlib import Path

from tts_utils import piper_text_to_speech


def main(text_file: str, output_file: str) -> None:
    """Read ``text_file`` and create an audio file at ``output_file``."""
    text = Path(text_file).read_text()
    piper_text_to_speech(text, output_file)
    print(f"Audio saved to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text file to a spoken WAV audio file.")
    parser.add_argument("text_file", help="Path to the input text file")
    parser.add_argument("output_file", help="Path where the resulting WAV should be written")
    args = parser.parse_args()

    main(args.text_file, args.output_file)
