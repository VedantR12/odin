from ddgs import DDGS

def search_web(query):

    try:

        results = DDGS().text(
            query,
            max_results=3
        )

        formatted = []

        for r in results:

            title = r.get("title", "")

            body = r.get("body", "")

            formatted.append(
                f"{title}: {body[:300]}"
            )

        return {
            "success": True,
            "data": "\n".join(formatted)
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }