def detect_tool(query):

    query = query.lower()

    # weather
    weather_keywords = [
        "weather",
        "temperature",
        "forecast",
        "humidity",
        "rain"
    ]

    # finance
    finance_keywords = [
        "stock",
        "bitcoin",
        "crypto",
        "market",
        "sensex",
        "nifty",
        "share price"
    ]

    # maps / roads
    maps_keywords = [
        "road",
        "traffic",
        "route",
        "map",
        "location",
        "construction",
        "signal"
    ]

    # geopolitics / news
    news_keywords = [
        "war",
        "president",
        "prime minister",
        "cm",
        "government",
        "iran",
        "israel",
        "news",
        "latest",
        "today"
    ]

    # wiki / people
    wiki_keywords = [
        "who is",
        "tell me about",
        "history",
        "information about"
    ]

    for word in weather_keywords:
        if word in query:
            return "weather"

    for word in finance_keywords:
        if word in query:
            return "finance"

    for word in maps_keywords:
        if word in query:
            return "maps"

    for word in news_keywords:
        if word in query:
            return "news"

    for word in wiki_keywords:
        if word in query:
            return "wiki"

    return "chat"