def policy_node(state):
    auto_resolve = ["PASSWORD_RESET"]

    if state["intent"] in auto_resolve:
        action = "AUTO_RESOLVE"
    else:
        action = "CREATE_TICKET"

    return {**state, "action": action}
