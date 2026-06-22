# AgriGuardian AI 🌾

## Overview

AgriGuardian AI is a multi-agent agricultural decision support system built using Google's Agent Development Kit (ADK).

The system helps farmers make informed decisions by combining:

* Farm registration and profiling
* Weather monitoring
* Soil analysis
* Crop market analysis
* Intelligent farming recommendations

The objective is to improve crop productivity, profitability, and sustainable farming practices.

---

## Features

### Land Agent

Collects and validates:

* State
* District
* Village
* Land size
* Irrigation type
* Current crop

### Weather Agent

Provides:

* Current weather conditions
* Temperature
* Humidity
* Farming precautions

### Soil Agent

Analyzes:

* Soil pH
* Nitrogen level
* Phosphorus level
* Potassium level

Provides soil improvement recommendations.

### Market Agent

Analyzes crop price data and identifies profitable crops.

### Advisory Agent

Combines:

* Soil information
* Weather information
* Market information

and generates farming recommendations.

---

## Architecture

Coordinator Agent

* Land Agent
* Weather Agent
* Soil Agent
* Market Agent
* Advisory Agent

Supporting Tools:

* Weather Tool
* Soil Analysis Tool
* Market Analysis Tool

External Services:

* OpenWeather API
* MCP Weather Server

---

## Technologies Used

* Python
* Google ADK
* Gemini 2.5 Flash
* MCP (Model Context Protocol)
* OpenWeather API
* GitHub

---

## Security

* API keys stored in `.env`
* No credentials committed to GitHub
* Modular tool architecture

---

## Project Structure

app/agri_guardian/

* agent.py
* models/
* sub_agents/
* tools/

mcp/

* weather_mcp_server.py

datasets/

* crop_prices.csv

docs/

* ROADMAP.md
* TASKS.md
* ARCHITECTURE.md

---

## Future Enhancements

* Government soil database integration
* Real-time crop market prices
* Fertilizer recommendation engine
* Pest and disease prediction
* Satellite and rainfall analysis

---

## Author

Nikhil
