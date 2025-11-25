import reflex as rx


class AppState(rx.State):
    """Global application state for EMRK Manager."""

    is_dark: bool = False
    environments: list[str] = ["Production", "Staging", "Development", "Air-gapped"]
    current_env: str = "Production"
    engines: list[str] = ["All Engines", "Engine-Alpha", "Engine-Beta", "Engine-Gamma"]
    selected_engine: str = "All Engines"
    menu_items: list[dict[str, str]] = [
        {"label": "Dashboard", "icon": "layout-dashboard", "path": "/"},
        {"label": "Engines", "icon": "server", "path": "/engines"},
        {"label": "Clusters", "icon": "database", "path": "/clusters"},
        {"label": "Nodes", "icon": "network", "path": "/nodes"},
        {"label": "Jobs", "icon": "activity", "path": "/jobs"},
        {"label": "Telemetry", "icon": "bar-chart-2", "path": "/telemetry"},
        {"label": "Logs", "icon": "file-text", "path": "/logs"},
        {"label": "Settings", "icon": "settings", "path": "/settings"},
    ]

    @rx.var
    def current_path(self) -> str:
        """Derive the current active sidebar path from the router."""
        current_route = self.router.page.path
        if current_route == "/":
            return "/"
        for item in self.menu_items:
            path = item["path"]
            if path != "/" and current_route.startswith(path):
                return path
        return "/"

    @rx.event
    def toggle_theme(self):
        self.is_dark = not self.is_dark

    @rx.event
    def set_env(self, env: str):
        self.current_env = env

    @rx.event
    def set_engine(self, engine: str):
        self.selected_engine = engine

    @rx.event
    def navigate(self, path: str):
        return rx.redirect(path)

    @rx.var
    def bg_color(self) -> str:
        return "bg-slate-900" if self.is_dark else "bg-gray-50"

    @rx.var
    def text_color(self) -> str:
        return "text-white" if self.is_dark else "text-gray-900"

    @rx.var
    def card_bg_color(self) -> str:
        return (
            "bg-slate-800 border-slate-700"
            if self.is_dark
            else "bg-white border-gray-200"
        )

    @rx.var
    def sub_text_color(self) -> str:
        return "text-slate-400" if self.is_dark else "text-gray-500"

    @rx.var
    def border_color(self) -> str:
        return "border-slate-700" if self.is_dark else "border-gray-200"