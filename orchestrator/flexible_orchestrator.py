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

    def route_request(self, user_input: str) -> str:
        intent = self.classify_intent(user_input)
        agent = self.agents.get(intent)
        if not agent:
            return "🤖 Sorry, I couldn't understand that request."
        return agent.handle(user_input)