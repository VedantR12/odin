import sounddevice as sd
from faster_whisper import WhisperModel
import numpy as np
import scipy.io.wavfile as wav

from vad import has_speech

# -------------------------
# LOAD MODEL
# -------------------------

print("Loading Whisper model...")

model = WhisperModel(
    "small",
    device="cuda",
    compute_type="int8"
)


print("Whisper model loaded!")

# -------------------------
# RECORD AUDIO
# -------------------------

def listen():

    RATE = 16000

    print("\nListening...")

    audio_chunks = []

    recording = False

    silence_counter = 0

    while True:

        chunk = sd.rec(
            int(0.5 * RATE),
            samplerate=RATE,
            channels=1,
            dtype='float32'
        )

        sd.wait()

        chunk = chunk.flatten()

        # speech detected
        if has_speech(chunk):

            recording = True

            silence_counter = 0

            audio_chunks.extend(chunk)

            print("Speech detected...")

        else:

            # after speech started
            if recording:

                silence_counter += 1

                audio_chunks.extend(chunk)

                # stop after silence
                if silence_counter > 3:
                    break

    # -------------------------
    # SAVE AUDIO
    # -------------------------

    audio = np.array(audio_chunks)

    wav.write(
        "input.wav",
        RATE,
        (audio * 32767).astype(np.int16)
    )

    # -------------------------
    # WHISPER
    # -------------------------

    print("Processing speech...")

    segments, info = model.transcribe(
        "input.wav",
        beam_size=5,
        vad_filter=True,
        language="en"
    )

    text = ""

    for segment in segments:

        text += segment.text

    text = text.strip()

    print("\nYou:", text)

    return text