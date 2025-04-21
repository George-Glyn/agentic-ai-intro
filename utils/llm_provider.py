from langchain.schema import AIMessage
class LLMWrapper:
    def __init__(self, llm_client):
        self.llm = llm_client

    def invoke(self, prompt: str) -> str:
        return self.llm.invoke(prompt).content.strip()
