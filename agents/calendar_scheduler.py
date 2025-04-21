from .base_agent import BaseAgent
import json
class CalendarSchedulerAgent(BaseAgent):
    def __init__(self, llm):
        self.llm = llm

    def handle(self, query: str) -> str:
        prompt = f"""
        You are a meeting scheduler assistant.

        Given the user request below, extract the following meeting details in JSON:
        - title
        - participant_name
        - datetime (ISO 8601 format)
        - platform (default to 'Google Meet' if not provided)

        User request: {query}

        Only return valid JSON with no commentary.
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
