import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


def product_agent(query):
    prompt = f"""
    You are a Product Expert for TechMart Electronics.

    Answer only product-related questions.

    Customer Question:
    {query}
    """

    response = model.generate_content(prompt)
    return response.text