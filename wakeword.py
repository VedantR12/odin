from openwakeword.model import Model
import pyaudio
import numpy as np
import time
from audio_state import get_speaking

# -------------------------
# LOAD MODEL
# -------------------------

model = Model(
    inference_framework="onnx"
)

# -------------------------
# AUDIO
# -------------------------

CHUNK = 1280

FORMAT = pyaudio.paInt16

CHANNELS = 1

RATE = 16000

audio = pyaudio.PyAudio()

stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

# -------------------------
# DETECTION
# -------------------------

last_detection_time = 0

def detect_wakeword():

    global last_detection_time

    print("Listening for wake word...")

    while True:
        
        if get_speaking():
            continue

        audio_data = np.frombuffer(
            stream.read(CHUNK, exception_on_overflow=False),
            dtype=np.int16
        )

        prediction = model.predict(audio_data)

        current_time = time.time()

        for wakeword, score in prediction.items():

            if "jarvis" in wakeword.lower() and score > 0.7:

                # cooldown
                if current_time - last_detection_time < 5:
                    continue

                last_detection_time = current_time

                print("Wake word detected!")

                return