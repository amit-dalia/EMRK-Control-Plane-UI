import reflex as rx


class DashboardState(rx.State):
    """State for the global dashboard."""

    total_engines: int = 4
    total_clusters: int = 48
    total_nodes: int = 156
    engines_with_alerts: int = 1
    heatmap_data: list[dict[str, str | int]] = [
        {"env": "Development", "Redis": 0, "Kafka": 0, "Postgres": 0, "ClickHouse": 0},
        {"env": "Staging", "Redis": 0, "Kafka": 1, "Postgres": 0, "ClickHouse": 0},
        {"env": "Production", "Redis": 0, "Kafka": 0, "Postgres": 0, "ClickHouse": 0},
        {"env": "Air-gapped", "Redis": 1, "Kafka": 2, "Postgres": 3, "ClickHouse": 3},
    ]
    heatmap_engines: list[str] = ["Redis", "Kafka", "Postgres", "ClickHouse"]
    recent_events: list[dict[str, str]] = [
        {
            "time": "10m ago",
            "env": "Production",
            "source": "Redis",
            "message": "Rolling upgrade completed successfully",
            "severity": "success",
        },
        {
            "time": "25m ago",
            "env": "Air-gapped",
            "source": "Kafka",
            "message": "Broker-2 connectivity lost",
            "severity": "error",
        },
        {
            "time": "1h ago",
            "env": "Staging",
            "source": "Redis",
            "message": "High memory usage detected on cluster-alpha",
            "severity": "warning",
        },
        {
            "time": "2h ago",
            "env": "Development",
            "source": "Postgres",
            "message": "New cluster provisioned",
            "severity": "info",
        },
    ]

    @rx.var
    def env_issues_count(self) -> int:
        return 2