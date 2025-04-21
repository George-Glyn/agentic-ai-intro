from .base_agent import BaseAgent
import json
from utils.date_utils import resolve_datetime

class CalendarSchedulerAgent(BaseAgent):
    def __init__(self, llm):
        self.llm = llm


    def handle(self, query: str) -> str:
        prompt = f"""Extract structured meeting data and return only valid JSON:
        {{
        "title": "...",
        "participant_name": "...",
        "datetime": "...",
        "platform": "..."
        }}
        Query: {query}
        """
        response = self.llm.invoke(prompt)
        if response.startswith("```json"):
            response = response.replace("```json", "").replace("```", "").strip()
        elif response.startswith("```"):
            response = response.replace("```", "").strip()

        try:
            parsed = json.loads(response)
            parsed["datetime"] = resolve_datetime(parsed["datetime"])
            return parsed
        except Exception:
            return {"error": "Failed to parse LLM response", "raw": response}
