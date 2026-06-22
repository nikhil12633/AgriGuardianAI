from google.adk.agents import Agent
from ..tools.soil_tool import analyze_soil

soil_agent = Agent(
    name="soil_agent",
    model="gemini-2.5-flash",
    description="Analyzes soil quality and provides recommendations",
    instruction="""
You are the Soil Agent.

Responsibilities:
- Analyze soil conditions.
- Explain soil health.
- Recommend improvements.
- Suggest suitable crops.

Use the soil analysis tool whenever soil data is provided.
""",
    tools=[analyze_soil]
)