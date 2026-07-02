import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


def technical_agent(query):
    prompt = f"""
    You are a Technical Support Engineer.

    Help customers solve technical problems related to electronics.

    Customer Question:
    {query}
    """

    response = model.generate_content(prompt)
    return response.text