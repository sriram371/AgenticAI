# IT Service Desk Agent (LangGraph-based)

This project is a **simple IT Service Desk automation prototype** built using **LangGraph** to demonstrate how agentic workflows can be orchestrated using a state graph.

The application connects a Slack bot to a LangGraph workflow that:
- Reads a user’s message from Slack
- Classifies the request using basic rule-based logic
- Decides whether the issue can be handled automatically or needs escalation
- Creates a Jira ticket for issues that require manual intervention

The goal of this project is to **practice and showcase LangGraph orchestration**, including state management, conditional routing, and tool invocation, rather than building a fully intelligent or production-ready support system.

---

## What the Application Does

1. A user mentions the bot in Slack with an IT-related message.
2. The message is passed into a LangGraph workflow.
3. The workflow:
   - Identifies the request type using simple keyword matching
   - Applies basic decision rules
   - Either marks the issue as resolved or creates a Jira ticket
4. The result is sent back to the user in Slack.

The intent detection and decision logic are intentionally kept simple and deterministic.

---

## Why LangGraph Is Used

LangGraph is used to model the workflow as an explicit graph instead of a linear script.  
This makes it easier to:
- See each step in the workflow
- Route execution based on decisions
- Add or modify steps later (for example, approvals or retries)

---

## Limitations

- Intent detection is rule-based and not learned or adaptive
- No real-time user clarification or follow-up questions
- No memory across conversations
- Designed for learning and experimentation, not production use

---

## Purpose of This Project

- Learn how to build agentic workflows using LangGraph
- Practice integrating multiple systems (Slack and Jira)
- Understand conditional orchestration and tool execution
- Serve as a foundation that can later be enhanced with LLMs or additional agents
