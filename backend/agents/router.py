from agents.billing_agent import billing_agent
from agents.product_agent import product_agent
from agents.technical_agent import technical_agent
from agents.complaint_agent import complaint_agent
from agents.faq_agent import faq_agent


def route_query(query):

    q = query.lower()

    if any(word in q for word in ["refund", "payment", "invoice", "bill"]):
        return billing_agent(query)

    elif any(word in q for word in ["laptop", "phone", "product", "headphone", "keyboard", "mouse"]):
        return product_agent(query)

    elif any(word in q for word in ["error", "problem", "issue", "repair", "not working"]):
        return technical_agent(query)

    elif any(word in q for word in ["complaint", "angry", "bad", "poor"]):
        return complaint_agent(query)

    else:
        return faq_agent(query)