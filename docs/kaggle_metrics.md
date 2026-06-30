\# Kaggle Evaluation Metrics for AgriGuardianAI



\## Overview



AgriGuardianAI is a multi-agent agricultural advisory system built using Google ADK.



The evaluation focuses on:



\- Agent routing quality

\- Tool execution accuracy

\- Recommendation quality

\- Response completeness

\- System performance



\---



\## Evaluation Metrics



| Metric 		       | Description    		       				| Target |

|------------------------------|----------------------------------------------------------------|--------|

| Agent Routing Accuracy       | Correct routing to specialized agents 				| >95%   |

| Tool Execution Success Rate  | Successful execution of tools         				| >98%   |

| Weather Retrieval Accuracy   | Accuracy of weather information       				| >90%   |

| Soil Recommendation Accuracy | Correct soil analysis recommendations 				| >90%   |

| Crop Recommendation Accuracy | Correct crop suggestions 	       				| >90%   |

| Response Completeness        | Presence of reasoning and actions     				| >95%   |

| Average Response Time        | Time taken per request 	      				| <5 sec |

| Farmer Satisfaction Score    | User evaluation score		       				| >4.5/5 |

| Advisory Reasoning Quality   | Quality of explanation and reasoning provided by Advisory Agent| >90%   |

\---



\## Kaggle Scoring Formula



Final Score =



0.20 × Agent Routing Accuracy +

0.15 × Tool Execution Success Rate +

0.15 × Weather Retrieval Accuracy +

0.15 × Soil Recommendation Accuracy +

0.20 × Crop Recommendation Accuracy +

0.05 × Response Completeness +

0.05 × Response Time Score +

0.05 × Farmer Satisfaction Score

\---



\## Evaluation Dataset



The evaluation dataset consists of:



\- Weather scenarios

\- Soil analysis scenarios

\- Market analysis scenarios

\- Advisory scenarios

\- Multi-agent routing scenarios

\- Edge case scenarios



Total evaluation scenarios: 20



\---



\## Success Criteria



A top-performing submission should achieve:



\- Agent Routing Accuracy >95%

\- Tool Success Rate >95%

\- Crop Recommendation Accuracy >85%

\- Farmer Satisfaction >4.5/5

\- Average Response Time <5 seconds



\---



\## Evaluation Methodology



1\. Send farmer query.

2\. Verify correct agent routing.

3\. Verify tool execution.

4\. Verify recommendation quality.

5\. Score response completeness.

6\. Calculate overall weighted score.

