from app.graph import it_service_desk_graph

def run_graph(user_id, text):
    initial_state = {
        "user_id": user_id,
        "user_message": text,
        "intent": None,
        "action": None,
        "jira_ticket": None
    }

    return it_service_desk_graph.invoke(initial_state)