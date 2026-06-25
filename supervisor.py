from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def supervisor(state):

    # Approval wale cases
    if state["approval_required"]:

        if state["approval_status"] == "Rejected":
            state["final_response"] = (
                "Your request requires supervisor approval. "
                "Unfortunately, the request was rejected."
            )
            return state

        prompt = f"""
You are a professional customer support supervisor.

Customer Query:
{state["query"]}

Retrieved Context:
{state["retrieved_context"]}

Draft Response:
{state["final_response"]}

Improve the response professionally.
Return only the final response.
"""

        response = llm.invoke(prompt)
        state["final_response"] = response.content
        return state

    # Normal Queries (No Approval Required)

    prompt = f"""
You are a professional customer support assistant.

Customer Query:
{state["query"]}

Retrieved Context:
{state["retrieved_context"]}

Draft Response:
{state["final_response"]}

Improve the response professionally.
Return only the final response.
"""

    response = llm.invoke(prompt)
    state["final_response"] = response.content

    return state