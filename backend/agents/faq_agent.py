import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def faq_agent(query):

    prompt = f"""
    You are the FAQ assistant for TechMart Electronics.

    Answer customer questions politely and clearly.

    Customer Question:
    {query}
    """

    response = model.generate_content(prompt)

    return response.text