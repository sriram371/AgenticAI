from fastapi import FastAPI, Request
from slack_bolt.adapter.fastapi import SlackRequestHandler
from slack_bolt import App
import os
from dotenv import load_dotenv

from app.slack_entry import run_graph

load_dotenv()
slack_app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

handler = SlackRequestHandler(slack_app)
api = FastAPI()

@slack_app.event("app_mention")
def handle_message(event, say):
    user_id = event["user"]
    text = event["text"]

    result = run_graph(user_id, text)

    if result.get("jira_ticket"):
        say(f"🎫 Ticket created: {result['jira_ticket']}")
    else:
        say("✅ Issue resolved automatically.")

@api.post("/slack/events")
async def slack_events(req: Request):
    return await handler.handle(req)

@api.get("/")
def health():
    return {"status": "running"}