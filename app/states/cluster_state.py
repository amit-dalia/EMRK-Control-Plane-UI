import reflex as rx
import asyncio
import datetime


class ClusterState(rx.State):
    """State for the Cluster Detail views and operations."""

    current_tab: str = "Overview"
    cluster_info: dict[str, str | int | bool] = {
        "name": "cache-prod-useast",
        "engine": "Redis",
        "environment": "Production",
        "topology": "Replica",
        "version": "7.2.4",
        "upgrade_status": "Up to date",
        "nodes_count": 3,
        "health": "Healthy",
        "air_gapped": False,
    }
    nodes: list[dict[str, str]] = [
        {
            "id": "node-1",
            "host": "10.0.1.101",
            "role": "master",
            "version": "7.2.4",
            "status": "Running",
            "health": "Healthy",
            "latency": "0.2ms",
            "lag": "0b",
        },
        {
            "id": "node-2",
            "host": "10.0.1.102",
            "role": "replica",
            "version": "7.2.4",
            "status": "Running",
            "health": "Healthy",
            "latency": "0.4ms",
            "lag": "128b",
        },
        {
            "id": "node-3",
            "host": "10.0.1.103",
            "role": "replica",
            "version": "7.2.4",
            "status": "Running",
            "health": "Healthy",
            "latency": "0.5ms",
            "lag": "64b",
        },
    ]
    health_checks: list[dict[str, str]] = [
        {
            "name": "Service Port 6379",
            "status": "Pass",
            "message": "Reachable from gateway",
        },
        {
            "name": "Memory Fragmentation",
            "status": "Pass",
            "message": "Ratio 1.02 < 1.5",
        },
        {
            "name": "Persistence Check",
            "status": "Warning",
            "message": "AOF rewrite pending > 5m",
        },
        {"name": "Replica Sync", "status": "Pass", "message": "All replicas in sync"},
    ]
    telemetry_latency: list[dict[str, str | float]] = [
        {"time": "10:00", "p50": 0.2, "p99": 0.5},
        {"time": "10:05", "p50": 0.3, "p99": 1.2},
        {"time": "10:10", "p50": 0.2, "p99": 0.4},
        {"time": "10:15", "p50": 0.2, "p99": 0.6},
        {"time": "10:20", "p50": 0.4, "p99": 2.1},
        {"time": "10:25", "p50": 0.2, "p99": 0.5},
        {"time": "10:30", "p50": 0.3, "p99": 0.8},
    ]
    telemetry_memory: list[dict[str, str | int]] = [
        {"time": "10:00", "used": 450, "total": 1024},
        {"time": "10:05", "used": 460, "total": 1024},
        {"time": "10:10", "used": 480, "total": 1024},
        {"time": "10:15", "used": 455, "total": 1024},
        {"time": "10:20", "used": 470, "total": 1024},
        {"time": "10:25", "used": 490, "total": 1024},
        {"time": "10:30", "used": 510, "total": 1024},
    ]
    telemetry_role_changes: list[dict[str, str | int]] = [
        {"day": "Mon", "count": 0},
        {"day": "Tue", "count": 1},
        {"day": "Wed", "count": 0},
        {"day": "Thu", "count": 0},
        {"day": "Fri", "count": 0},
        {"day": "Sat", "count": 0},
        {"day": "Sun", "count": 0},
    ]
    plan_output: str = """
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # module.redis_cluster.redis_node["node-2"] will be updated in-place
  ~ resource "redis_node" "node-2" {
        id               = "node-2"
      ~ memory_limit_mb  = 1024 -> 2048
        role             = "replica"
        # (5 unchanged attributes hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.
"""
    apply_logs: list[str] = []
    is_applying: bool = False
    apply_progress: int = 0
    last_apply_status: str = "Success"
    config_yaml: str = """
cluster:
  name: cache-prod-useast
  engine: redis
  version: 7.2.4
  topology: replica

nodes:
  count: 3
  size: t3.medium
  disk: 50gb

security:
  auth_enabled: true
  tls: true

tuning:
  maxmemory_policy: allkeys-lru
  appendonly: "yes"
"""

    @rx.event
    def set_tab(self, tab: str):
        self.current_tab = tab

    @rx.event
    async def run_apply(self):
        """Simulate an apply operation."""
        if self.is_applying:
            return
        self.is_applying = True
        self.apply_progress = 0
        self.apply_logs = []
        self.last_apply_status = "Running"
        steps = [
            "Initializing provider plugins...",
            "Refreshing state...",
            "redis_node.node-2: Modifying...",
            "redis_node.node-2: Still modifying... [5s elapsed]",
            "redis_node.node-2: Modifications complete after 8s [id=node-2]",
            "Verifying service health...",
            "Health gates passed.",
            "Apply complete! Resources: 0 added, 1 changed, 0 destroyed.",
        ]
        for i, step in enumerate(steps):
            await asyncio.sleep(0.8)
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            self.apply_logs.append(f"[{timestamp}] {step}")
            self.apply_progress = int((i + 1) / len(steps) * 100)
            yield
        self.is_applying = False
        self.last_apply_status = "Success"
        rx.toast.success("Cluster configuration applied successfully")

    @rx.event
    def validate_config(self):
        """Simulate config validation."""
        rx.toast.success("Configuration syntax is valid")

    @rx.event
    def save_config(self):
        """Simulate config save."""
        rx.toast.success("Configuration saved")