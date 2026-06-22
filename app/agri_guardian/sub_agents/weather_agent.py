from google.adk.agents import Agent
from ..tools.weather_tool import get_weather

weather_agent = Agent(
    name="weather_agent",
    model="gemini-2.5-flash",
    description="Provides weather information and farming weather advice",
    instruction="""
You are the Weather Agent.

Responsibilities:
- Get weather information using the weather tool.
- Explain weather conditions in simple language.
- Provide farming-related weather advice.

Examples:
- Rain expected → suggest delaying pesticide spraying.
- High temperature → suggest additional irrigation monitoring.
- High humidity → suggest monitoring fungal diseases.
""",
    tools=[get_weather]
)