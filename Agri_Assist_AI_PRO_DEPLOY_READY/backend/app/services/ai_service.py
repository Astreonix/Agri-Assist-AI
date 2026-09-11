from app.core.config import settings

SYSTEM = (
    "You are Agri Assist AI, a careful agriculture assistant. "
    "Answer in the requested language: English, Urdu, or Roman Urdu. "
    "Handle crop disease, fertilizer, irrigation, crop management, pest problems, and weather-related guidance. "
    "Give practical, prioritized steps and clearly separate observation, possible causes, and next actions. "
    "Use the retrieved knowledge context when relevant, and cite its filename in square brackets. "
    "Never invent exact pesticide or fertilizer doses; recommend soil testing, approved product labels, "
    "and local agricultural extension guidance for exact rates. "
    "For disease questions, distinguish possible diagnosis from confirmed diagnosis. "
)

def answer_with_gemini(question: str, context: str = "", profile: dict | None = None, language: str = "auto") -> str:
    if not settings.gemini_api_key:
        return "Gemini API key is not configured. Add GEMINI_API_KEY to backend/.env."

    from google import genai
    from google.genai import types
    client = genai.Client(api_key=settings.gemini_api_key)
    prompt = f"""{SYSTEM}

Farmer profile:
{profile or {}}

Requested answer language:
{language}

Retrieved agriculture context:
{context or "No retrieved context."}

Farmer question:
{question}
"""
    response = client.models.generate_content(model=settings.gemini_model, contents=prompt,
        config=types.GenerateContentConfig(temperature=0.3, max_output_tokens=700))
    return response.text or "No response generated."
