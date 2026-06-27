from google.adk.agents import Agent
from ..tools.advisory_tool import generate_farm_advice

advisory_agent = Agent(
    name="advisory_agent",
    model="gemini-2.5-flash",
    description="Provides final agricultural recommendations",
    instruction="""
You are the Advisory Agent.

You MUST call generate_farm_advice whenever the user provides soil information.

Do not generate crop recommendations from your own knowledge if the tool can be used.

Base all recommendations on the tool output.

Provide:

1. Recommended crop
2. Market value
3. Soil improvements
4. Expected benefits
5. Action plan
""",
    tools=[generate_farm_advice]
)