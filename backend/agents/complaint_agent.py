import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


def complaint_agent(query):
    prompt = f"""
    You are a Complaint Resolution Officer.

    Respond politely and professionally to customer complaints.

    Customer Complaint:
    {query}
    """

    response = model.generate_content(prompt)
    return response.text