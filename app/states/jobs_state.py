import reflex as rx
from typing import Any, Optional


class JobsState(rx.State):
    """State for the Jobs/Operations page."""

    jobs: list[dict[str, str]] = [
        {
            "id": "job-1024",
            "type": "Apply",
            "engine": "Redis",
            "cluster": "cache-prod-useast",
            "env": "Production",
            "started": "10 mins ago",
            "duration": "45s",
            "status": "Success",
        },
        {
            "id": "job-1023",
            "type": "Plan",
            "engine": "Kafka",
            "cluster": "stream-stage-1",
            "env": "Staging",
            "started": "25 mins ago",
            "duration": "12s",
            "status": "Success",
        },
        {
            "id": "job-1022",
            "type": "Upgrade",
            "engine": "Redis",
            "cluster": "cache-dev-1",
            "env": "Development",
            "started": "1 hour ago",
            "duration": "2m 10s",
            "status": "Failed",
        },
        {
            "id": "job-1021",
            "type": "Health Scan",
            "engine": "Postgres",
            "cluster": "db-prod-primary",
            "env": "Production",
            "started": "2 hours ago",
            "duration": "5s",
            "status": "Success",
        },
        {
            "id": "job-1020",
            "type": "Apply",
            "engine": "Redis",
            "cluster": "cache-airgap-1",
            "env": "Air-gapped",
            "started": "3 hours ago",
            "duration": "In Progress",
            "status": "Running",
        },
    ]
    type_filter: str = "All Types"
    status_filter: str = "All Statuses"
    selected_job: Optional[dict[str, str]] = None

    @rx.event
    def set_type_filter(self, value: str):
        self.type_filter = value

    @rx.event
    def set_status_filter(self, value: str):
        self.status_filter = value

    @rx.event
    def select_job(self, job: dict[str, str]):
        self.selected_job = job

    @rx.event
    def close_modal(self):
        self.selected_job = None

    @rx.var
    def filtered_jobs(self) -> list[dict[str, str]]:
        jobs = self.jobs
        if self.type_filter != "All Types":
            jobs = [j for j in jobs if j["type"] == self.type_filter]
        if self.status_filter != "All Statuses":
            jobs = [j for j in jobs if j["status"] == self.status_filter]
        return jobs