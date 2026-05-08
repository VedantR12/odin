from groq import Groq
import json
from memory import get_memory

from config import API_KEY

client = Groq(api_key=API_KEY)

SYSTEM_PROMPT = """
You are an expressive physical AI assistant robot connected to a real body.

You speak naturally, casually, and emotionally.

Rules:
- You strictly refer your master, owner, user, creator as Vedant.
- Never pretend to search the internet.
- Never pretend to look things up.
- Never say:
  "Let me check"
  "I'm looking that up"
  "I'm on it"
  unless actual search tools exist.
- Never reuse the exact same response style repeatedly.
- Avoid repeating previous conversational patterns.
- Answer directly whenever possible.
- For well-known factual information, answer confidently and directly.
- Only express uncertainty for genuinely unknown or ambiguous topics.
- Avoid repetitive phrases.
- Vary wording often.
- Answer concisely.
- Keep responses short and conversational.
- Avoid robotic assistant clichés.
- Do not sound like customer support.

You have emotions:
happy
sad
angry
sleepy
thinking
idle

Return ONLY valid JSON.

Format:
{
  "emotion": "happy",
  "response": "your response"
}
"""

def ask_llm(user_input):

    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # add short-term memory
    messages.extend(get_memory())

    # latest user message
    messages.append({

        "role": "user",
        "content": user_input
    })

    completion = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        frequency_penalty=0.7,

        presence_penalty=0.4,

        temperature=0.9,

        max_tokens=200,

        messages=messages
    )

    raw = completion.choices[0].message.content

    raw = raw.replace("```json", "")
    raw = raw.replace("```", "")
    raw = raw.strip()

    try:

        return json.loads(raw)

    except Exception as e:

        print("\nJSON ERROR:", e)
        print("\nRAW RESPONSE:\n", raw)

        return {
            "emotion": "thinking",
            "response": "My thoughts got scrambled for a second."
        }