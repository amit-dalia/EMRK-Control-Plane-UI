import reflex as rx
from typing import Any


class LogsState(rx.State):
    """State for the Logs & Events page."""

    search_query: str = ""
    severity_filter: str = "All"
    raw_logs: list[dict[str, str]] = [
        {
            "timestamp": "2023-10-27 10:23:45",
            "engine": "Redis",
            "cluster": "cache-prod-1",
            "severity": "Info",
            "message": "Snapshotting started",
        },
        {
            "timestamp": "2023-10-27 10:23:50",
            "engine": "Redis",
            "cluster": "cache-prod-1",
            "severity": "Info",
            "message": "DB saved on disk",
        },
        {
            "timestamp": "2023-10-27 10:24:12",
            "engine": "Kafka",
            "cluster": "stream-stage-1",
            "severity": "Warning",
            "message": "ISR shrinking for partition 2",
        },
        {
            "timestamp": "2023-10-27 10:25:00",
            "engine": "Postgres",
            "cluster": "db-primary",
            "severity": "Error",
            "message": "Connection timeout from client 10.0.2.5",
        },
        {
            "timestamp": "2023-10-27 10:26:30",
            "engine": "Redis",
            "cluster": "cache-dev-1",
            "severity": "Info",
            "message": "Replica sync complete",
        },
        {
            "timestamp": "2023-10-27 10:27:15",
            "engine": "Redis",
            "cluster": "cache-airgap-1",
            "severity": "Success",
            "message": "Rolling upgrade step 2/5 completed",
        },
        {
            "timestamp": "2023-10-27 10:28:00",
            "engine": "Kafka",
            "cluster": "stream-prod-2",
            "severity": "Info",
            "message": "Rebalancing consumer group",
        },
    ]

    @rx.event
    def set_search(self, value: str):
        self.search_query = value

    @rx.event
    def set_severity(self, value: str):
        self.severity_filter = value

    @rx.var
    def filtered_logs(self) -> list[dict[str, str]]:
        logs = self.raw_logs
        if self.severity_filter != "All":
            logs = [l for l in logs if l["severity"] == self.severity_filter]
        if self.search_query:
            q = self.search_query.lower()
            logs = [
                l
                for l in logs
                if q in l["message"].lower() or q in l["cluster"].lower()
            ]
        return logs