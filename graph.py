from langgraph.graph import StateGraph, END
from state import CustomerSupportState
from agents import (
    classify_intent,
    route_department,
    sales_agent,
    technical_agent,
    billing_agent,
    account_agent,
    check_approval
)
from approval import human_approval
from supervisor import supervisor

builder = StateGraph(CustomerSupportState)

# ------------------ Nodes ------------------

builder.add_node("Intent", classify_intent)
builder.add_node("Routing", route_department)

builder.add_node("Sales", sales_agent)
builder.add_node("Technical", technical_agent)
builder.add_node("Billing", billing_agent)
builder.add_node("Account", account_agent)

builder.add_node("Approval Check", check_approval)
builder.add_node("Human Approval", human_approval)

builder.add_node("Supervisor", supervisor)

# ------------------ Entry Point ------------------

builder.set_entry_point("Intent")

builder.add_edge("Intent", "Routing")

# ------------------ Department Routing ------------------

def select_agent(state):
    return state["department"]

builder.add_conditional_edges(
    "Routing",
    select_agent,
    {
        "Sales": "Sales",
        "Technical": "Technical",
        "Billing": "Billing",
        "Account": "Account"
    }
)

# ------------------ Go to Approval Check ------------------

builder.add_edge("Sales", "Approval Check")
builder.add_edge("Technical", "Approval Check")
builder.add_edge("Billing", "Approval Check")
builder.add_edge("Account", "Approval Check")

# ------------------ Approval Routing ------------------

def approval_router(state):
    if state["approval_required"]:
        return "yes"
    return "no"

builder.add_conditional_edges(
    "Approval Check",
    approval_router,
    {
        "yes": "Human Approval",
        "no": "Supervisor"
    }
)

# ------------------ Final Flow ------------------

builder.add_edge("Human Approval", "Supervisor")
builder.add_edge("Supervisor", END)

# ------------------ Compile ------------------

graph = builder.compile()