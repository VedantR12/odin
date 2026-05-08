VALID_EMOTIONS = [
    "happy",
    "thinking",
    "sleepy",
    "idle",
    "talking"
]

def clean_emotion(emotion):

    if emotion in VALID_EMOTIONS:
        return emotion

    return "idle"