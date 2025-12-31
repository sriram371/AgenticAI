from app.tools.jira_tool import create_ticket

def jira_node(state):
    ticket = create_ticket(
        summary=f"IT Issue: {state['intent']}",
        description=state["user_message"]
    )

    return {**state, "jira_ticket": ticket}
