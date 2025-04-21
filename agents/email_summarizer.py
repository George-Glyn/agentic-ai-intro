from .base_agent import BaseAgent

class EmailSummarizerAgent(BaseAgent):
    def __init__(self, llm):
        self.llm = llm

    def handle(self, query: str) -> str:
        prompt = f"Summarize the following email: {query}"
        return self.llm.invoke(prompt)