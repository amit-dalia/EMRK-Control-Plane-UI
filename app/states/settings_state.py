import reflex as rx
from typing import Any


class SettingsState(rx.State):
    """State for the Settings/Admin page."""

    api_url: str = "https://api.emrk-manager.internal"
    auth_scheme: str = "Bearer Token"
    environments: list[dict[str, str]] = [
        {"name": "Development", "type": "Cloud", "regions": "us-east-1"},
        {"name": "Staging", "type": "Cloud", "regions": "us-east-1"},
        {"name": "Production", "type": "Hybrid", "regions": "us-east-1, eu-west-1"},
        {"name": "Air-gapped", "type": "On-Prem", "regions": "datacenter-1"},
    ]
    plugins: list[dict[str, str | bool]] = [
        {
            "name": "Redis Engine",
            "version": "1.2.0",
            "enabled": True,
            "author": "EMRK Corp",
        },
        {
            "name": "Kafka Engine",
            "version": "2.1.0",
            "enabled": True,
            "author": "EMRK Corp",
        },
        {
            "name": "Postgres Engine",
            "version": "1.5.4",
            "enabled": True,
            "author": "Community",
        },
        {
            "name": "ClickHouse Engine",
            "version": "0.9.2",
            "enabled": False,
            "author": "Labs",
        },
    ]

    @rx.event
    def toggle_plugin(self, name: str):
        for p in self.plugins:
            if p["name"] == name:
                p["enabled"] = not p["enabled"]

    @rx.event
    def save_api_config(self):
        rx.toast.success("API Configuration Saved")