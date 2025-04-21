import json
from fastapi.responses import JSONResponse

class FlexibleOrchestrator:
    def __init__(self, llm, agent_registry: dict):
        self.llm = llm
        self.agents = agent_registry

    def classify_intent(self, user_input: str) -> str:
        prompt = f"""
        Classify this input into one of the following intents:
        - summarize_email
        - create_task
        - schedule_meeting
        - lookup_data

        Input: "{user_input}"
        """
        intent = self.llm.invoke(prompt).lower()
        return intent if intent in self.agents else "fallback"

    def route_request(self, query: str) -> str:
        intent = self.classify_intent(query)
        agent = self.agents.get(intent)
        if not agent:
            return "🤖 Sorry, I couldn't understand that request."

        try:
            result = json.loads(agent.handle(query))
            return result
        except json.JSONDecodeError:
            return JSONResponse(
                status_code=422,
                content={"error": "LLM response was not valid JSON", "raw": agent.handle(query)}
            )
