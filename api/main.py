from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator.flexible_orchestrator import FlexibleOrchestrator
from utils.llm_provider import LLMWrapper

# Import agents
from agents.email_summarizer import EmailSummarizerAgent
from agents.task_creator import TaskCreatorAgent
from agents.calendar_scheduler import CalendarSchedulerAgent
from agents.data_lookup import DataLookupAgent

from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from fastapi.responses import FileResponse

# Initialize environment variables
load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", api_key=os.environ["GOOGLE_API_KEY"]
)

llm_provider = LLMWrapper(llm)

# Agent Registry
agent_registry = {
    "summarize_email": EmailSummarizerAgent(llm_provider),
    "create_task": TaskCreatorAgent(llm_provider),
    "schedule_meeting": CalendarSchedulerAgent(llm_provider),
    "lookup_data": DataLookupAgent(llm_provider),
}

app = FastAPI()
orchestrator = FlexibleOrchestrator(llm_provider, agent_registry)


class RequestBody(BaseModel):
    query: str


@app.get("/")
def frontend():
    return FileResponse(os.path.join("web", "index.html"))


@app.post("/agentic/copilot")
def route_query(body: RequestBody):
    return {"result": orchestrator.route_request(body.query)}
