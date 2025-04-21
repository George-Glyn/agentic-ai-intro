from .base_agent import BaseAgent
import re
import json

class TaskCreatorAgent(BaseAgent):
    def __init__(self, llm):
        self.llm = llm

    def handle(self, query: str) -> str:
        prompt = f"""
        You're a task creation agent. Based on the user's request, output the task in JSON format.

        Required keys:
        - title
        - description
        - due_date
        - priority
        - subtasks (list of strings)

        Input: {query}

        Only output JSON. Do not include commentary.
        """
        response = self.llm.invoke(prompt)
        # Validate JSON response
        if response.startswith("```json"):
            response = response.replace("```json", "").replace("```", "").strip()
        elif response.startswith("```"):
            response = response.replace("```", "").strip()

        return response