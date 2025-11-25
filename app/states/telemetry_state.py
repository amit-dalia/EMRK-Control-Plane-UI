import reflex as rx
from typing import Any


class TelemetryState(rx.State):
    """State for the Global Telemetry page."""

    time_range: str = "1h"
    selected_engine: str = "All Engines"
    latency_data: list[dict[str, str | float]] = [
        {"time": "10:00", "Redis": 0.5, "Kafka": 2.1, "Postgres": 5.4},
        {"time": "10:05", "Redis": 0.6, "Kafka": 2.3, "Postgres": 5.1},
        {"time": "10:10", "Redis": 0.8, "Kafka": 2.0, "Postgres": 6.2},
        {"time": "10:15", "Redis": 0.5, "Kafka": 2.5, "Postgres": 5.8},
        {"time": "10:20", "Redis": 1.2, "Kafka": 3.1, "Postgres": 5.5},
        {"time": "10:25", "Redis": 0.6, "Kafka": 2.2, "Postgres": 5.3},
        {"time": "10:30", "Redis": 0.5, "Kafka": 2.1, "Postgres": 5.2},
    ]
    ops_data: list[dict[str, str | int]] = [
        {"time": "10:00", "ops": 12000},
        {"time": "10:05", "ops": 15000},
        {"time": "10:10", "ops": 13500},
        {"time": "10:15", "ops": 18000},
        {"time": "10:20", "ops": 16000},
        {"time": "10:25", "ops": 14500},
        {"time": "10:30", "ops": 15500},
    ]
    error_rate_data: list[dict[str, str | int]] = [
        {"cluster": "cache-prod", "errors": 12},
        {"cluster": "stream-prod", "errors": 5},
        {"cluster": "db-prod", "errors": 2},
        {"cluster": "cache-dev", "errors": 0},
        {"cluster": "db-stage", "errors": 8},
    ]

    @rx.event
    def set_time_range(self, value: str):
        self.time_range = value

    @rx.event
    def set_engine(self, value: str):
        self.selected_engine = value