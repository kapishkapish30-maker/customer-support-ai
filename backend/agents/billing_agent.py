import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


def billing_agent(query):
    prompt = f"""
    You are a Billing Support Agent for TechMart Electronics.

    Help customers regarding:
    - Refunds
    - Payments
    - Billing
    - Invoices

    Customer Question:
    {query}
    """

    response = model.generate_content(prompt)
    return response.text