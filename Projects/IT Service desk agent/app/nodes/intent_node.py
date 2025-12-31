def intent_node(state):
    text = state["user_message"].lower()

    if "password" in text:
        intent = "PASSWORD_RESET"
    elif "vpn" in text:
        intent = "VPN_ISSUE"
    elif "access" in text:
        intent = "ACCESS_REQUEST"
    else:
        intent = "UNKNOWN"

    return {**state, "intent": intent}
