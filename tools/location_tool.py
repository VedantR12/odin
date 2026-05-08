import re

def extract_city(text):

    text = text.lower()

    patterns = [

        r"weather in ([a-zA-Z\s]+?)(?:\?|$)",
        r"temperature in ([a-zA-Z\s]+?)(?:\?|$)",
        r"forecast for ([a-zA-Z\s]+?)(?:\?|$)",
        r"in ([a-zA-Z\s]+?)(?:\?|$)"
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:

            city = match.group(1).strip()

            return city.title()

    # default city
    return "Delhi"
