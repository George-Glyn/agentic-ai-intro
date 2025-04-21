from .base_agent import BaseAgent
import json
class CalendarSchedulerAgent(BaseAgent):
    def __init__(self, llm):
        self.llm = llm

    def handle(self, query: str) -> str:
        prompt = f"""
        Extract structured meeting data from the following input and return valid JSON with these fields:

        - title
        - participant_name
        - datetime (in ISO 8601 format)
        - platform (default to "Google Meet" if not specified)

        User input: {query}

        Only return JSON. No Markdown, no natural language.
        """

        response = self.llm.invoke(prompt)
        # Validate JSON response
        if response.startswith("```json"):
            response = response.replace("```json", "").replace("```", "").strip()
        elif response.startswith("```"):
            response = response.replace("```", "").strip()
            
        return response