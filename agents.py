from rag import retrieve
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from memory import save_memory, get_memory

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def classify_intent(state):
    query = state["query"]

    prompt = f"""
    Classify the customer query into ONLY one category:
    Sales
    Technical
    Billing
    Account

    Query: {query}

    Return only the category name.
    """

    response = llm.invoke(prompt)

    state["intent"] = response.content.strip()
    return state

def route_department(state):
    intent = state["intent"]

    if intent == "Sales":
        state["department"] = "Sales"

    elif intent == "Technical":
        state["department"] = "Technical"

    elif intent == "Billing":
        state["department"] = "Billing"

    elif intent == "Account":
        state["department"] = "Account"

    return state

print("agents.py loaded")

def sales_agent(state):
    context = retrieve(state["query"])
    state["retrieved_context"] = context
    state["final_response"] = context
    return state


def technical_agent(state):
    context = retrieve(state["query"])
    state["retrieved_context"] = context
    state["final_response"] = context
    return state


def billing_agent(state):
    context = retrieve(state["query"])
    state["retrieved_context"] = context
    state["final_response"] = context
    return state


def account_agent(state):

    previous = get_memory(state["customer_name"])

    context = retrieve(state["query"])

    prompt = f"""
    Previous Conversation:
    {previous}

    Context:
    {context}

    Customer Question:
    {state["query"]}

    Give a professional answer.
    """

    response = llm.invoke(prompt)

    state["memory"] = previous
    state["retrieved_context"] = context
    state["final_response"] = response.content

    save_memory(
        state["customer_name"],
        state["query"],
        state["final_response"]
    )

    return state

def check_approval(state):

    query = state["query"].lower()

    keywords = [
        "refund",
        "cancel subscription",
        "account closure",
        "close account",
        "compensation"
    ]

    state["approval_required"] = any(word in query for word in keywords)

    return state