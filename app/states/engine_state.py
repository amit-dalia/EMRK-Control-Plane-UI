import reflex as rx


class EngineState(rx.State):
    """State for Engine management and details."""

    current_tab: str = "Overview"
    tabs: list[str] = [
        "Overview",
        "Clusters",
        "Telemetry",
        "Logs & Events",
        "Plugin Info",
    ]

    @rx.event
    def set_tab(self, tab: str):
        self.current_tab = tab

    engines: list[dict[str, str | int | list[str]]] = [
        {
            "id": "redis",
            "name": "Redis",
            "plugin_id": "plugin-redis-v1.2",
            "version": "7.2.4",
            "clusters": 12,
            "nodes": 48,
            "last_scan": "2 mins ago",
            "status": "Healthy",
            "environments": ["Dev", "Stage", "Prod", "Air-gapped"],
            "description": "In-memory data structure store, used as a database, cache, and message broker.",
        },
        {
            "id": "kafka",
            "name": "Kafka",
            "plugin_id": "plugin-kafka-v2.0",
            "version": "3.6.0",
            "clusters": 5,
            "nodes": 15,
            "last_scan": "5 mins ago",
            "status": "Warning",
            "environments": ["Dev", "Stage", "Prod"],
            "description": "Distributed event streaming platform.",
        },
        {
            "id": "postgres",
            "name": "Postgres",
            "plugin_id": "plugin-pg-v1.5",
            "version": "16.1",
            "clusters": 24,
            "nodes": 48,
            "last_scan": "1 min ago",
            "status": "Healthy",
            "environments": ["Dev", "Prod"],
            "description": "Advanced open source relational database.",
        },
        {
            "id": "clickhouse",
            "name": "ClickHouse",
            "plugin_id": "plugin-ch-v0.9",
            "version": "23.8",
            "clusters": 2,
            "nodes": 8,
            "last_scan": "1 hour ago",
            "status": "Critical",
            "environments": ["Air-gapped"],
            "description": "Fast open-source OLAP database management system.",
        },
    ]
    clusters: list[dict[str, str | int]] = [
        {
            "name": "cache-prod-useast",
            "env": "Production",
            "topology": "Cluster",
            "nodes": 6,
            "health": "Healthy",
            "last_op": "Apply (Success)",
        },
        {
            "name": "queue-stage-1",
            "env": "Staging",
            "topology": "Sentinel",
            "nodes": 3,
            "health": "Healthy",
            "last_op": "Plan (No changes)",
        },
        {
            "name": "store-dev-alpha",
            "env": "Development",
            "topology": "Single",
            "nodes": 1,
            "health": "Warning",
            "last_op": "Apply (Failed)",
        },
        {
            "name": "cache-airgap-1",
            "env": "Air-gapped",
            "topology": "Replica",
            "nodes": 2,
            "health": "Healthy",
            "last_op": "Upgrade (Success)",
        },
    ]

    @rx.var
    def current_engine(self) -> dict[str, str | int | list[str]]:
        """Get the engine details based on the current URL parameter."""
        engine_id = self.router.page.params.get("engine_id", "redis")
        return next((e for e in self.engines if e["id"] == engine_id), self.engines[0])

    @rx.var
    def current_engine_status_color(self) -> str:
        status = self.current_engine.get("status", "Unknown")
        if status == "Healthy":
            return "text-emerald-500"
        if status == "Warning":
            return "text-amber-500"
        if status == "Critical":
            return "text-red-500"
        return "text-gray-500"