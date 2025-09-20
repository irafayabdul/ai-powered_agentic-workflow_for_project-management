from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"

# Instantiate a KnowledgeAugmentedPromptAgent
knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona,
    knowledge=knowledge
)

# Get the agent's response
agent_response = knowledge_agent.respond(prompt)

# Print the response and a confirmation message
print(agent_response)
print("\nThe agent's response is based on the provided knowledge, not its own.")
