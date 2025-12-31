from typing import TypedDict, Optional

class ITState(TypedDict):
    user_id: str
    user_message: str
    intent: Optional[str]
    action: Optional[str]
    jira_ticket: Optional[str]