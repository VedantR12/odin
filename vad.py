from silero_vad import load_silero_vad
from silero_vad import get_speech_timestamps

import torch

model = load_silero_vad()

def has_speech(audio):

    audio_tensor = torch.tensor(
        audio,
        dtype=torch.float32
    )

    speech = get_speech_timestamps(
        audio_tensor,
        model
    )

    return len(speech) > 0