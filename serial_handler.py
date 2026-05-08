import serial
import time
from config import SERIAL_PORT

esp = serial.Serial(SERIAL_PORT, 115200)

time.sleep(2)

def send_emotion(emotion):

    esp.write((emotion + "\n").encode())