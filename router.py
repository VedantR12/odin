LIVE_KEYWORDS = [

    # time-sensitive
    "current",
    "today",
    "latest",
    "live",
    "recent",
    "now",
    "currently",

    # politics
    "prime minister",
    "pm",
    "president",
    "vice president",
    "home minister",
    "cm",
    "chief minister",
    "governor",
    "minister",
    "election",
    "government",
    "politics",

    # news
    "news",
    "headline",
    "update",
    "breaking",

    # weather
    "weather",
    "temperature",
    "rain",
    "forecast",
    "humidity",

    # finance
    "stock",
    "share price",
    "bitcoin",
    "crypto",
    "market",
    "nifty",
    "sensex",
    "price",

    # sports
    "score",
    "match",
    "ipl",
    "football",
    "cricket",
    "winner",
    "won",

    # tech
    "release",
    "launch",
    "new version",
    "update version",

    # geography / public info
    "population",
    "capital",
    "currency",

    # celebrities / public figures
    "age",
    "net worth",
    "wife",
    "husband",

    # factual lookup indicators
    "who is",
    "what is",
    "tell me about"
]

def needs_live_info(text):

    text = text.lower()

    for keyword in LIVE_KEYWORDS:

        if keyword in text.lower():
            return True

    return False