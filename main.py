from llm import ask_llm
from tts import speak
import time
from state_manager import set_state
from idle_animation import start_idle_animation
from tools.router import detect_tool
from tools.search_tool import search_web
from tools.weather_tool import get_weather
from serial_handler import send_emotion
from emotions import clean_emotion
from stt import listen
from wakeword import detect_wakeword
from tools.news_tool import search_news
from tools.wiki_tool import search_wiki
from tools.geopolitics_tool import geopolitics_search
from tools.location_tool import extract_city
from memory import add_memory

start_idle_animation()

while True:

    set_state("idle")
    send_emotion("idle")

    # wait for wake word
    detect_wakeword()

    set_state("listening")
    send_emotion("listening")

    user_input = listen()

    if not user_input or len(user_input.strip()) < 2:
        continue

    add_memory("user", user_input)
    set_state("thinking")
    send_emotion("thinking")
    
    tool = detect_tool(user_input)
    
    print("\nTOOL:", tool)

    live_context = ""

    # -------------------------
    # WEATHER TOOL
    # -------------------------

    if tool == "weather":
        
        city = extract_city(user_input)

        weather = get_weather(city)

        if weather["success"]:

            w = weather["data"]

            live_context = f"""
                Current weather in {w['location']}:

                Temperature:
                {w['temperature']}°C

                Humidity:
                {w['humidity']}%

                Condition:
                {w['weather']}
                """
        else:

            response = weather["error"]

            print("\nBot:", response)
            
            send_emotion("sad")

            set_state("talking")
            send_emotion("talking")

            speak(response)

            continue

    # -------------------------
    # SEARCH TOOL
    # -------------------------

    elif tool == "news":

        results = search_news(user_input)
    
        if results["success"]:
        
            live_context = results["data"]
    
        else:
        
            print("\nNews Tool Error:",
                  results["error"])
    
    elif tool == "wiki":
    
        results = search_wiki(user_input)
    
        if results["success"]:
        
            live_context = results["data"]
    
        else:
        
            print("\nWiki Tool Error:",
                  results["error"])
    
    elif tool == "geopolitics":
    
        results = geopolitics_search(user_input)
    
        if results["success"]:
        
            live_context = results["data"]
    
        else:
        
            print("\nGeopolitics Tool Error:",
                  results["error"])

    if live_context:

        enhanced_input = f"""
    Use the live information below to answer naturally.

    User question:
    {user_input}

    Live information:
    {live_context}
    """

        data = ask_llm(enhanced_input)

    else:

        data = ask_llm(user_input)

    emotion = clean_emotion(data["emotion"])

    response = data["response"]

    print("\nBot:", response)

    send_emotion(emotion)

    set_state("talking")
    send_emotion("talking")

    speak(response)
    add_memory("assistant", response)

    send_emotion("idle")