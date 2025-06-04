"""Helper utilities for synthesizing speech via ``edge-tts``."""

import asyncio
from typing import List

import edge_tts

MAX_CHARS = 4000


def _split_text(text: str, max_chars: int = MAX_CHARS) -> List[str]:
    """Split ``text`` into chunks not exceeding ``max_chars``.

    Splitting priority is as follows: two newlines (``"\n\n"``), single
    newline, sentence punctuation (``. ! ?``), spaces and finally hard splits
    if none of the above produce short enough chunks.
    """
    if len(text) <= max_chars:
        return [text]

    separators = ["\n\n", "\n", ".", "!", "?", " ", ""]
    chunks: List[str] = []
    length = len(text)
    start = 0

    while start < length:
        end = min(start + max_chars, length)
        cut = None
        for sep in separators:
            if sep:
                idx = text.rfind(sep, start, end)
                if idx != -1 and idx + len(sep) <= end and idx >= start:
                    cut = idx + len(sep)
                    break
            else:
                cut = end
        if cut is None or cut <= start:
            cut = end

        chunk = text[start:cut].strip()
        if chunk:
            chunks.append(chunk)
        start = cut

    return chunks


async def _synthesize_chunk(chunk: str, voice: str, rate: str, volume: str, pitch: str) -> bytes:
    communicator = edge_tts.Communicate(text=chunk, voice=voice, rate=rate, volume=volume, pitch=pitch)
    audio_bytes = bytearray()
    async for msg in communicator.stream():
        if msg["type"] == "audio":
            audio_bytes.extend(msg["data"])
    return bytes(audio_bytes)


async def text_to_speech_async(
    text: str,
    output_file: str,
    voice: str = "en-US-AriaNeural",
    rate: str = "+0%",
    volume: str = "+0%",
    pitch: str = "+0Hz",
) -> None:
    """Convert text to speech using edge-tts.

    The text is split into sensible chunks (4000 chars by default) to avoid
    service limits. The resulting audio is saved to ``output_file``.
    """
    chunks = _split_text(text, MAX_CHARS)
    with open(output_file, "wb") as f:
        for chunk in chunks:
            audio = await _synthesize_chunk(chunk, voice, rate, volume, pitch)
            f.write(audio)


def text_to_speech(
    text: str,
    output_file: str,
    voice: str = "en-US-AriaNeural",
    rate: str = "+0%",
    volume: str = "+0%",
    pitch: str = "+0Hz",
) -> None:
    """Synchronous wrapper around :func:`text_to_speech_async`."""
    asyncio.run(text_to_speech_async(text, output_file, voice, rate, volume, pitch))
