from .base_agent import BaseAgent

class EmailSummarizerAgent(BaseAgent):
    def __init__(self, llm):
        self.llm = llm

    def handle(self, query: str) -> str:
        prompt = f"""
        Summarize the following email into clear JSON format.

        Required format:
        {{
        "summary": "..."
        }}

        Email content: {query}

        Only output valid JSON.
        """
        response = self.llm.invoke(prompt)
        # Validate JSON response
        if response.startswith("```json"):
            response = response.replace("```json", "").replace("```", "").strip()
        elif response.startswith("```"):
            response = response.replace("```", "").strip()

        return response