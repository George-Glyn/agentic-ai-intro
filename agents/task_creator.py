from .base_agent import BaseAgent
import re
import json

class TaskCreatorAgent(BaseAgent):
    def __init__(self, llm):
        self.llm = llm

    def handle(self, query: str) -> str:

        prompt = f"""
        You are a task creation AI. Given the following instruction, return a concise JSON for a task creation system with fields:

        - title
        - description
        - due_date
        - priority
        - subtasks (list of strings)

        Instruction: {query}

        Only return valid JSON.
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