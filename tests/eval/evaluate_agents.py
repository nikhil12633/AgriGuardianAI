import json
from tests.eval.metrics import EvaluationMetrics

metrics = EvaluationMetrics()

# Example scenario evaluations

scenarios = [
    {
        "name": "Weather Query",
        "expected_agent": "weather_agent",
        "actual_agent": "weather_agent",
        "success": True
    },
    {
        "name": "Soil Query",
        "expected_agent": "soil_agent",
        "actual_agent": "soil_agent",
        "success": True
    },
    {
        "name": "Market Query",
        "expected_agent": "market_agent",
        "actual_agent": "market_agent",
        "success": True
    }
]

for scenario in scenarios:

    metrics.total_cases += 1

    if scenario["expected_agent"] == scenario["actual_agent"]:
        metrics.correct_routes += 1

    if scenario["success"]:
        metrics.tool_success += 1
        metrics.complete_responses += 1

results = {
    "agent_routing_accuracy":
        metrics.routing_accuracy(),

    "tool_execution_success":
        metrics.tool_success_rate(),

    "response_completeness":
        metrics.response_completeness(),

    "average_response_time":
        metrics.average_response_time()
}

print(json.dumps(results, indent=2))