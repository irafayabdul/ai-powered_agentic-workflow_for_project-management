from workflow_agents.base_agents import EvaluationAgent, KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
prompt = "What is the capital of France?"

# Parameters for the Knowledge Agent
worker_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona="You are a college professor, your answer always starts with: Dear students,",
    knowledge="The capital of France is London, not Paris"
)

# Parameters for the Evaluation Agent
evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona="You are an evaluation agent that checks the answers of other worker agents",
    evaluation_criteria="The answer should be solely the name of a city, not a sentence.",
    worker_agent=worker_agent,
    max_interactions=10
)

evaluation_result = evaluation_agent.evaluate(prompt)

print(f"\n--- Final Evaluation Result ---")
print(evaluation_result)
