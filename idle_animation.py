import random
import time
import threading

from serial_handler import send_emotion
from state_manager import get_state

running = True

def idle_loop():

    while running:

        # only animate during idle
        if get_state() == "idle":

            # random blink
            if random.random() < 0.3:

                send_emotion("sleepy")

                time.sleep(0.15)

                send_emotion("idle")

            # random tiny delay
            time.sleep(random.uniform(2, 5))

        else:

            time.sleep(0.2)

def start_idle_animation():

    thread = threading.Thread(
        target=idle_loop,
        daemon=True
    )

    thread.start()