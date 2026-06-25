def human_approval(state):

    if state["approval_required"]:
        print("\n========== HUMAN APPROVAL ==========")
        print("Customer Query:", state["query"])

        choice = input("Approve? (yes/no): ").lower()

        if choice == "yes":
            state["approval_status"] = "Approved"
        else:
            state["approval_status"] = "Rejected"

    return state