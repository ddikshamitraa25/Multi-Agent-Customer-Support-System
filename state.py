from typing import TypedDict


class CustomerSupportState(TypedDict):
    customer_name: str
    query: str
    intent: str
    department: str
    retrieved_context: str
    memory: str
    approval_required: bool
    approval_status: str
    final_response: str