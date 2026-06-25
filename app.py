from graph import graph

state = {
    "customer_name": "David",
    "query": "What was my previous issue?",
    "intent": "",
    "department": "",
    "retrieved_context": "",
    "memory": "",
    "approval_required": False,
    "approval_status": "",
    "final_response": ""
}

result = graph.invoke(state)

print("\nIntent:", result["intent"])
print("Department:", result["department"])

print("\nPrevious Memory:")
print(result["memory"])

print("\nFinal Response:")
print(result["final_response"])