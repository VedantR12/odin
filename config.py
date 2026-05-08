import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

SERIAL_PORT = "COM3"

PIPER_PATH = r"C:\piper\piper.exe"

MODEL_PATH = r"C:\piper\models\lessac-medium.onnx"