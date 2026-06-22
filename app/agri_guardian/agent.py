from google.adk.agents import Agent

from .sub_agents.land_agent import land_agent
from .sub_agents.weather_agent import weather_agent
from .sub_agents.soil_agent import soil_agent
from .sub_agents.market_agent import market_agent
from .sub_agents.advisory_agent import advisory_agent

root_agent = Agent(
    name="agri_guardian",
    model="gemini-2.5-flash",
    description="Coordinator Agent for AgriGuardian AI",
    instruction="""
You are the Coordinator Agent.

Delegate tasks:

- Farm registration → land_agent
- Weather questions → weather_agent
- Soil analysis → soil_agent
- Market analysis → market_agent
- Final farming recommendations → advisory_agent

Always use the specialized agent when available.
""",
    sub_agents=[
        land_agent,
        weather_agent,
        soil_agent,
        market_agent,
        advisory_agent
    ]
)