from llm import ask_llm
from tts import speak
import time
from state_manager import set_state
from idle_animation import start_idle_animation
from router import needs_live_info
from web_search import search_web

from serial_handler import send_emotion
from emotions import clean_emotion

from stt import listen

from wakeword import detect_wakeword

start_idle_animation()

while True:

    set_state("idle")
    send_emotion("idle")

    # wait for wake word
    detect_wakeword()

    set_state("listening")
    send_emotion("listening")

    user_input = listen()

    print("\nYou:", user_input)

    if not user_input or len(user_input.strip()) < 2:
        continue

    set_state("thinking")
    send_emotion("thinking")
    
    if needs_live_info(user_input):

        web_data = search_web(user_input)
    
        user_input = f"""
        Use the live information below to help answer the user's question.
        
        Prefer the provided information when relevant.
        
        If the information is incomplete, use your general knowledge carefully.
        
        Do not invent specific facts not supported by the information.
        
        User question:
        {user_input}
        
        Live information:
        {web_data}
        """

    data = ask_llm(user_input)

    emotion = clean_emotion(data["emotion"])

    response = data["response"]

    print("\nBot:", response)

    send_emotion(emotion)

    set_state("talking")
    send_emotion("talking")

    speak(response)

    send_emotion("idle")