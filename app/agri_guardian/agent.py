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
You are the AgriGuardian coordinator.

Routing rules:

1. If user asks ONLY about soil properties,
   route to soil_agent.

2. If user asks about crop recommendation,
   farming advice,
   market profitability,
   best crop,
   or provides season + soil + nutrients,
   ALWAYS route to advisory_agent.

3. Weather questions:
   weather_agent.

4. Land registration:
   land_agent.

5. Market price only:
   market_agent.

IMPORTANT:
Final farming recommendation requests MUST NEVER go to soil_agent.
""",

    sub_agents=[
        land_agent,
        weather_agent,
        soil_agent,
        market_agent,
        advisory_agent
    ]
)