\# AgriGuardianAI System Architecture



\## Overview



AgriGuardianAI is a Google Agent Development Kit (ADK) based multi-agent agricultural advisory system designed to assist farmers with:



\- Weather analysis

\- Soil analysis

\- Market profitability analysis

\- Crop recommendation

\- Final farming advisory



The system follows a Google ADK Coordinator/Sub-Agent multi-agent architecture, where specialized agents collaborate to provide agricultural decision support.





\## Architecture Diagram



&#x20;                    +------------------+

&#x20;                   |      Farmer      |

&#x20;                   +---------+--------+

&#x20;                             |

&#x20;                             v

&#x20;                +-------------------------+

&#x20;                |    Coordinator Agent    |

&#x20;                +-----------+-------------+

&#x20;                            |

&#x20;       +---------+----------+----------+----------+

&#x20;       |         |          |          |          |

&#x20;       v         v          v          v          v

+-----------+ +---------+ +--------+ +--------+ +----------+

| Land      | | Weather | | Soil   | | Market | | Advisory |

| Agent     | | Agent   | | Agent  | | Agent  | | Agent    |

+-----+-----+ +----+----+ +----+---+ +----+---+ +-----+----+

&#x20;     |            |           |          |            |

&#x20;     v            v           v          v            v

+-----------+ +----------+ +---------+ +----------+ +---------+

| Farm      | | Weather  | | Soil    | | Market   | | Advisory|

| Profile   | | Tool     | | Tool    | | Tool     | | Tool    |

+-----------+ +-----+----+ +---------+ +-----+----+ +---------+

&#x20;                   |

&#x20;                   v

&#x20;          +----------------+

&#x20;          | OpenWeather API|

&#x20;          +----------------+



&#x20;          +----------------+

&#x20;          | MCP Weather    |

&#x20;          | Server         |

&#x20;          +----------------+





\## Components



\### Coordinator Agent

Responsible for routing farmer queries to the appropriate specialized agent.



\### Weather Agent

Provides weather information using the Weather Tool and OpenWeather API.



\### Soil Agent

Analyzes soil pH and nutrient values and provides recommendations.



\### Market Agent

Analyzes profitability using crop market datasets.



\### Advisory Agent

Combines weather, soil, and market insights to generate final farming recommendations.



\### MCP Weather Server

Provides weather retrieval through the Model Context Protocol.







\## Workflow



1\. Farmer submits a query.

2\. Coordinator Agent identifies the required specialized agents.

3\. Weather Agent retrieves weather information using OpenWeather API or MCP Weather Server.

4\. Soil Agent analyzes soil pH and nutrient values.

5\. Market Agent analyzes crop profitability using local datasets.

6\. Advisory Agent combines weather, soil, and market insights.

7\. Advisory Tool generates the final agricultural recommendation.

8\. The final recommendation is returned to the farmer.





\## Design Pattern



\- Google ADK Multi-Agent Architecture

\- Coordinator/Sub-Agent Pattern

\- Tool-Augmented Agents

\- Model Context Protocol (MCP) Integration

\- Rule-Based Agricultural Decision Support System

