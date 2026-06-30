# AgriGuardianAI

AgriGuardianAI is a Google Agent Development Kit (ADK) based multi-agent agricultural advisory system designed to help farmers make informed decisions using weather, soil, and market analysis.

---

## Features

- Multi-agent architecture using Google ADK
- Coordinator agent for intelligent routing
- Weather analysis using OpenWeather API
- Soil health analysis
- Crop profitability analysis
- Agricultural advisory generation
- MCP Weather Server integration
- Evaluation framework
- Unit and integration testing

---

## Architecture

AgriGuardianAI follows a Coordinator/Sub-Agent architecture.

Agents:

- Coordinator Agent
- Land Agent
- Weather Agent
- Soil Agent
- Market Agent
- Advisory Agent

Tools:

- Weather Tool
- Soil Tool
- Market Tool
- Advisory Tool

---

## Project Structure

app/
agri_guardian/
├── agent.py
├── models/
├── sub_agents/
└── tools/

tests/
├── unit/
├── integration/
└── eval/

docs/

datasets/



---

## Multi-Agent Workflow

Farmer Query

↓

Coordinator Agent

↓

Land Agent
Weather Agent
Soil Agent
Market Agent

↓

Advisory Agent

↓

Final Recommendation

---

## Evaluation

Current evaluation metrics:

- Agent Routing Accuracy
- Tool Execution Success
- Response Completeness
- Response Time

Current score:

- Agent Routing Accuracy: 100%
- Tool Success: 100%
- Response Completeness: 100%

---

## Unit Tests
pytest tests/unit -v

Results:
20 passed


---

## Technologies Used

- Google ADK
- Gemini 2.5 Flash
- Python
- FastAPI
- OpenWeather API
- MCP Server
- Pytest

---

## Future Improvements

- Persistent farm profiles
- Weather forecasting
- Historical market trends
- Irrigation recommendations
- Fertilizer recommendations
- Frontend dashboard
- Multi-language support

---

## Authors

Nikhil
AgriGuardianAI Capstone Project
