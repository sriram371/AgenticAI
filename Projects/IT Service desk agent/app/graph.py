from langgraph.graph import StateGraph, END
from app.state import ITState

from app.nodes.intent_node import intent_node
from app.nodes.policy_node import policy_node
from app.nodes.jira_node import jira_node
from app.nodes.resolution_node import resolution_node

graph = StateGraph(ITState)

graph.add_node("intent", intent_node)
graph.add_node("policy", policy_node)
graph.add_node("jira", jira_node)
graph.add_node("resolve", resolution_node)

graph.set_entry_point("intent")

graph.add_edge("intent", "policy")

def route_action(state):
    return state["action"]

graph.add_conditional_edges(
    "policy",
    route_action,
    {
        "AUTO_RESOLVE": "resolve",
        "CREATE_TICKET": "jira"
    }
)

graph.add_edge("jira", END)
graph.add_edge("resolve", END)

it_service_desk_graph = graph.compile()
