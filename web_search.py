from ddgs import DDGS

def clean_text(text):

    text = text.replace("\n", " ")

    text = text.strip()

    return text

def search_web(query):

    results = DDGS().text(query, max_results=3)

    compressed = []

    for r in results:

        title = clean_text(
            r.get("title", "")
        )

        body = clean_text(
            r.get("body", "")
        )

        # keep snippets short
        body = body[:400]

        compressed.append(
            f"{title}: {body}"
        )

    return "\n".join(compressed)