from .base_agent import BaseAgent
import json
class DataLookupAgent(BaseAgent):
    def __init__(self, llm):
        self.llm = llm

    def handle(self, query: str) -> str:
        prompt = f"""
        Return factual data based on this query in JSON format.

        Example input: "What is John Doe's last submitted timesheet date?"

        Expected output format:
        {{
        "employee_name": "John Doe",
        "last_submitted_timesheet_date": "YYYY-MM-DD"
        }}

        Query: {query}

        Output only valid JSON.
        """
        response = self.llm.invoke(prompt)
        # Validate JSON response
        if response.startswith("```json"):
            response = response.replace("```json", "").replace("```", "").strip()
        elif response.startswith("```"):
            response = response.replace("```", "").strip()

        return response