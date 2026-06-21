from google.adk.agents import Agent
from .sub_agents.land_agent import land_agent

root_agent = Agent(
    name="agri_guardian",
    model="gemini-2.5-flash",
    description="Coordinator agent for AgriGuardian AI",
    instruction="""
You are the Coordinator Agent.

Responsibilities:
- Understand the farmer's request.
- Delegate farm-information collection tasks to land_agent.
- Never collect farm details yourself if land_agent can handle it.

Use specialized agents whenever possible.
""",
    sub_agents=[land_agent]
)