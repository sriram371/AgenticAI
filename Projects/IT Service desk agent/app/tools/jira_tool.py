import os, requests
from requests.auth import HTTPBasicAuth

def create_ticket(summary, description):
    url = f"{os.getenv('JIRA_BASE_URL')}/rest/api/3/issue"
    auth = HTTPBasicAuth(
        os.getenv("JIRA_EMAIL"),
        os.getenv("JIRA_API_TOKEN")
    )

    payload = {
        "fields": {
            "project": {"key": os.getenv("JIRA_PROJECT_KEY")},
            "summary": summary,
            "issuetype": {"name": "Task"}
        }
    }

    r = requests.post(url, json=payload, auth=auth)
    r.raise_for_status()
    return r.json()["key"]