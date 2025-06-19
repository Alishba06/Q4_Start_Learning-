from agent import SmartAgent # type: ignore
from runner import BrainRunner

def dynamic_instructions():
    return "Guide the user with their fitness goals."

agent = SmartAgent(
    title="DailyFit AI",
    behavior=dynamic_instructions,
    model_type="gpt-4o"
)

user_question = "What should I do to stay fit today?"
BrainRunner.respond(agent, user_question)
