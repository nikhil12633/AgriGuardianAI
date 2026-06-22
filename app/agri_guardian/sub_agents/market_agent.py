from google.adk.agents import Agent
from ..tools.market_tool import get_best_crop

market_agent = Agent(
    name="market_agent",
    model="gemini-2.5-flash",
    description="Analyzes crop market prices and recommends profitable crops",
    instruction="""
You are the Market Agent.

Responsibilities:
- Analyze crop market prices.
- Identify profitable crops.
- Explain recommendations to farmers.
- Use the market tool whenever market analysis is requested.
""",
    tools=[get_best_crop]
)