import time


class EvaluationMetrics:
    def __init__(self):
        self.total_cases = 0
        self.correct_routes = 0
        self.tool_success = 0
        self.weather_accuracy = 0
        self.soil_accuracy = 0
        self.crop_accuracy = 0
        self.complete_responses = 0
        self.response_times = []

    def add_response_time(self, seconds):
        self.response_times.append(seconds)

    def routing_accuracy(self):
        if self.total_cases == 0:
            return 0
        return self.correct_routes / self.total_cases

    def tool_success_rate(self):
        if self.total_cases == 0:
            return 0
        return self.tool_success / self.total_cases

    def weather_score(self):
        if self.total_cases == 0:
            return 0
        return self.weather_accuracy / self.total_cases

    def soil_score(self):
        if self.total_cases == 0:
            return 0
        return self.soil_accuracy / self.total_cases

    def crop_score(self):
        if self.total_cases == 0:
            return 0
        return self.crop_accuracy / self.total_cases

    def response_completeness(self):
        if self.total_cases == 0:
            return 0
        return self.complete_responses / self.total_cases

    def average_response_time(self):
        if not self.response_times:
            return 0
        return sum(self.response_times) / len(self.response_times)