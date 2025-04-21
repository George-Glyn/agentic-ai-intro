from .base_agent import BaseAgent
import json
class DataLookupAgent(BaseAgent):
    def __init__(self, llm):
        self.llm = llm

    def handle(self, query: str) -> str:
        prompt = f"""
        You are a structured data assistant.

        Given a query like:
        "What is John Doe's last submitted timesheet date?"

        Respond with JSON in this format:
        {{
        "employee_name": "John Doe",
        "last_submitted_timesheet_date": "YYYY-MM-DD"
        }}

        Only return valid JSON. Do not use Markdown or code blocks. Do not describe the response.
        Query: {query}
        """
        response = self.llm.invoke(prompt)
        # Validate JSON response
        if response.startswith("```json"):
            response = response.replace("```json", "").replace("```", "").strip()
        elif response.startswith("```"):
            response = response.replace("```", "").strip()

        try:
            task_data = json.loads(response)
            return task_data
        except json.JSONDecodeError:
            return "🤖 Sorry, I couldn't create a task from that instruction."
