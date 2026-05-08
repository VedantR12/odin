from ddgs import DDGS

def search_web(query):

    try:

        results = DDGS().text(
            query,
            max_results=5
        )

        formatted = []

        for r in results:

            title = r.get("title", "")

            body = r.get("body", "")

            formatted.append(
                f"Title: {title}\nSnippet: {body[:400]}"
            )

        return {
            "success": True,
            "data": "\n\n".join(formatted)
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }