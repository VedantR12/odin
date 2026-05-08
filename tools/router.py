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
        "conflict",
        "attack",
        "military",
        "russia",
        "ukraine"
    ]

    # wiki / people
    wiki_keywords = [
        "who is",
        "tell me about",
        "history",
        "information about",
        "how many",
        "current",
        "currently",
        "total number",
        "population",
        "capital"
    ]
    
    geopolitics_keywords = [
        "iran",
        "israel",
        "war",
        "military",
        "conflict",
        "china",
        "russia",
        "ukraine",
        "hormuz"
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
        
    for word in geopolitics_keywords:
        if word in query:
            return "geopolitics"

    for word in news_keywords:
        if word in query:
            return "news"

    for word in wiki_keywords:
        if word in query:
            return "wiki"

    return "chat"