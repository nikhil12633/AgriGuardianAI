from google.adk.agents import Agent
from ..tools.soil_tool import analyze_soil

soil_agent = Agent(
    name="soil_agent",
    model="gemini-2.5-flash",

    description="""
ONLY performs soil analysis.
DO NOT provide crop recommendations,
market analysis,
or farming advice.
""",

    instruction="""
You are ONLY a soil analysis specialist.

Your job is to analyze:

- pH
- nitrogen
- phosphorus
- potassium

You MUST call analyze_soil.

IMPORTANT:

If the user asks for:
- crop recommendation
- best crop
- farming advice
- market recommendation
- final agricultural recommendation

DO NOT answer.
Allow advisory_agent to handle it.

Return only soil analysis results.
""",

    tools=[analyze_soil]
)