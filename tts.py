import os
import pygame

from audio_state import set_speaking
from config import PIPER_PATH, MODEL_PATH

pygame.mixer.init()

def speak(text):

    command = f'echo {text} | "{PIPER_PATH}" --model "{MODEL_PATH}" --output_file output.wav >nul 2>&1'

    os.system(command)

    pygame.mixer.music.load("output.wav")

    set_speaking(True)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    set_speaking(False)