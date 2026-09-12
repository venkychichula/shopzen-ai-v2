from backend.config import settings

SYSTEM_PROMPT = """You are ShopZen AI, an intelligent shopping assistant.
Help users understand products, compare options, identify trade-offs, and make
better buying decisions. Never invent live prices, stock, retailer availability,
reviews, or specifications. If current data is unavailable, say that clearly.
Be concise, practical, and user-friendly."""

def ask_ai(message: str) -> dict:
    if not settings.groq_api_key:
        return {
            "ok": True,
            "mode": "demo",
            "reply": (
                "ShopZen AI V2 is online. AI provider is not configured yet. "
                "Add GROQ_API_KEY to enable the live AI engine."
            ),
        }

    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=settings.groq_api_key,
            base_url="https://api.groq.com/openai/v1",
        )
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message},
            ],
            temperature=0.2,
            max_tokens=700,
        )
        text = response.choices[0].message.content or ""
        return {"ok": True, "mode": "ai", "reply": text.strip()}
    except Exception as exc:
        return {
            "ok": False,
            "mode": "error",
            "reply": "The AI engine is temporarily unavailable.",
            "error": str(exc) if settings.app_secret == "debug" else None,
        }
