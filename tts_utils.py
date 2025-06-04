"""Helper utilities for synthesizing speech via ``piper``."""

import wave
from pathlib import Path
from typing import Optional

from piper import PiperVoice, download


def piper_text_to_speech(
    text: str,
    output_file: str,
    voice: str = "en_US-lessac-medium",
    model_dir: str = "piper_voices",
    speaker_id: Optional[int] = None,
    length_scale: Optional[float] = None,
    noise_scale: Optional[float] = None,
    noise_w: Optional[float] = None,
    sentence_silence: float = 0.0,
) -> None:
    """Convert ``text`` to speech using ``piper``.

    The required voice model is downloaded automatically into ``model_dir`` if
    missing. The resulting WAV audio is saved to ``output_file``.
    """

    voices_info = download.get_voices(model_dir)
    download.ensure_voice_exists(
        voice, data_dirs=[model_dir], download_dir=model_dir, voices_info=voices_info
    )

    model_path = Path(model_dir) / f"{voice}.onnx"
    config_path = Path(model_dir) / f"{voice}.onnx.json"
    piper_voice = PiperVoice.load(model_path, config_path)

    with wave.open(output_file, "wb") as wav_file:
        piper_voice.synthesize(
            text,
            wav_file,
            speaker_id=speaker_id,
            length_scale=length_scale,
            noise_scale=noise_scale,
            noise_w=noise_w,
            sentence_silence=sentence_silence,
        )
