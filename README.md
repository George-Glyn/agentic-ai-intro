# 🧠 Agentic AI Copilot

Agentic AI Copilot is a modular, LLM-powered orchestration system that uses intent classification to dynamically route user inputs to specialized agents. Perfect for enterprise-grade automation and intelligent workflow execution.

---

## 🚀 Features

- 🔄 Intent-based routing using LLMs
- 🤖 Specialized agents for summarization, task creation, scheduling, and data lookup
- 🧩 Extensible architecture (add new agents easily)
- ⚡ Built with FastAPI
- 🧠 Uses LangChain and OpenAI (or other LLM providers)

---

## 🗂️ Folder Structure

```
agentic_copilot/
├── agents/                # Specialized task agents
├── orchestrator/          # Core router logic
├── utils/                 # LLM wrapper
├── api/                   # FastAPI entry point
├── requirements.txt       # Project dependencies
└── README.md              # Project overview and usage
```

---

## 🧑‍💻 Installation

1. Clone the repo:
```bash
git clone https://github.com/your-org/agentic_copilot.git
cd agentic_copilot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your LLM credentials using `.env` or directly within `llm_provider.py`.

---

## ▶️ Run the API

```bash
uvicorn api.main:app --reload
```

API will be live at: `http://127.0.0.1:8000/agentic/copilot`

---

## 🧪 Sample API Call

**POST** `/agentic/copilot`

```json
{
  "query": "Summarize: The Q2 deadline is Friday. Please alert all teams."
}
```

**Response**
```json
{
  "result": "Summary: Q2 deadline is Friday. Notify all teams."
}
```

---

## 🧠 Agent Intents

| Intent             | Description                          |
|--------------------|--------------------------------------|
| summarize_email    | Summarize email content              |
| create_task        | Create actionable tasks              |
| schedule_meeting   | Set calendar meetings                |
| lookup_data        | Retrieve internal structured data    |

---

## 📌 Future Add-ons

- Memory store (PGVector or ChromaDB)
- Logging and analytics
- Web-based UI
- Docker support

---

## 🧑‍🔧 Author

Built by [George Glyn / Team] — Inspired by the rise of Agentic AI in enterprise automation.