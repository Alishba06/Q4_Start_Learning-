from agent import SmartAgent  # type: ignore

class BrainRunner:
    @classmethod
    def respond(cls, agent: SmartAgent, question: str):
        
        print(f"🤖 {agent.title} says: Based on '{question}', I suggest doing... push-ups!")
