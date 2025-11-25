import reflex as rx
from app.states.app_state import AppState
from app.states.dashboard_state import DashboardState


def summary_card(
    title: str,
    value: str | int,
    icon: str,
    trend: str | None = None,
    trend_color: str = "text-emerald-500",
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                title,
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-sm font-medium text-slate-400",
                    "text-sm font-medium text-gray-500",
                ),
            ),
            rx.icon(icon, class_name="w-5 h-5 text-teal-500 opacity-80"),
            class_name="flex justify-between items-start",
        ),
        rx.el.div(
            rx.el.span(
                value,
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-3xl font-bold text-white",
                    "text-3xl font-bold text-gray-900",
                ),
            ),
            rx.cond(
                trend != None,
                rx.el.span(trend, class_name=f"text-xs font-medium {trend_color} ml-2"),
            ),
            class_name="mt-4 flex items-baseline",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "p-6 rounded-xl bg-slate-800 border border-slate-700 shadow-sm hover:border-slate-600 transition-colors",
            "p-6 rounded-xl bg-white border border-gray-200 shadow-sm hover:border-gray-300 transition-colors",
        ),
    )


def heatmap_cell(status: int) -> rx.Component:
    """Render a heatmap cell based on status integer."""
    color_class = rx.match(
        status,
        (0, "bg-emerald-500/20 text-emerald-500 border-emerald-500/30"),
        (1, "bg-amber-500/20 text-amber-500 border-amber-500/30"),
        (2, "bg-red-500/20 text-red-500 border-red-500/30"),
        "bg-gray-500/20 text-gray-500 border-gray-500/30",
    )
    icon_name = rx.match(
        status,
        (0, "check-circle"),
        (1, "alert-triangle"),
        (2, "x-circle"),
        "help-circle",
    )
    return rx.el.div(
        rx.icon(icon_name, class_name="w-5 h-5"),
        class_name=rx.cond(
            AppState.is_dark,
            f"h-12 w-full rounded-md border flex items-center justify-center {color_class}",
            f"h-12 w-full rounded-md border flex items-center justify-center {color_class}",
        ),
    )


def env_heatmap_row(row: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.span(row["env"], class_name="font-medium"),
            class_name=rx.cond(
                AppState.is_dark, "py-3 text-slate-300", "py-3 text-gray-700"
            ),
        ),
        rx.foreach(
            DashboardState.heatmap_engines,
            lambda engine: rx.el.td(heatmap_cell(row[engine]), class_name="p-1"),
        ),
    )


def environment_heatmap() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Environment Status Matrix",
            class_name=rx.cond(
                AppState.is_dark,
                "text-lg font-semibold text-white mb-4",
                "text-lg font-semibold text-gray-900 mb-4",
            ),
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th("", class_name="w-32"),
                        rx.foreach(
                            DashboardState.heatmap_engines,
                            lambda e: rx.el.th(
                                e,
                                class_name=rx.cond(
                                    AppState.is_dark,
                                    "pb-2 text-xs font-medium text-slate-500 uppercase tracking-wider text-center",
                                    "pb-2 text-xs font-medium text-gray-400 uppercase tracking-wider text-center",
                                ),
                            ),
                        ),
                    )
                ),
                rx.el.tbody(rx.foreach(DashboardState.heatmap_data, env_heatmap_row)),
                class_name="w-full table-auto",
            ),
            class_name=rx.cond(
                AppState.is_dark,
                "p-6 rounded-xl bg-slate-800 border border-slate-700 shadow-sm",
                "p-6 rounded-xl bg-white border border-gray-200 shadow-sm",
            ),
        ),
    )


def recent_event_item(event: dict) -> rx.Component:
    icon_class = rx.match(
        event["severity"],
        ("success", "w-4 h-4 text-emerald-500"),
        ("warning", "w-4 h-4 text-amber-500"),
        ("error", "w-4 h-4 text-red-500"),
        "w-4 h-4 text-blue-500",
    )
    container_class = rx.match(
        event["severity"],
        (
            "success",
            "flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center bg-emerald-500/10",
        ),
        (
            "warning",
            "flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center bg-amber-500/10",
        ),
        (
            "error",
            "flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center bg-red-500/10",
        ),
        "flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center bg-blue-500/10",
    )
    icon_name = rx.match(
        event["severity"],
        ("success", "check"),
        ("warning", "alert-triangle"),
        ("error", "x-octagon"),
        "info",
    )
    return rx.el.div(
        rx.el.div(
            rx.icon(icon_name, class_name=icon_class), class_name=container_class
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(event["source"], class_name="font-bold mr-2"),
                rx.el.span(event["message"], class_name="font-medium"),
                class_name=rx.cond(
                    AppState.is_dark, "text-sm text-slate-200", "text-sm text-gray-900"
                ),
            ),
            rx.el.div(
                rx.el.span(event["env"], class_name="mr-2"),
                rx.el.span("•", class_name="mx-1 opacity-50"),
                rx.el.span(event["time"]),
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-xs text-slate-500 mt-0.5",
                    "text-xs text-gray-500 mt-0.5",
                ),
            ),
            class_name="flex-1 min-w-0",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "flex items-start gap-4 p-3 rounded-lg hover:bg-slate-700/50 transition-colors",
            "flex items-start gap-4 p-3 rounded-lg hover:bg-gray-50 transition-colors",
        ),
    )


def recent_events_list() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Recent Activity",
            class_name=rx.cond(
                AppState.is_dark,
                "text-lg font-semibold text-white mb-4",
                "text-lg font-semibold text-gray-900 mb-4",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.foreach(DashboardState.recent_events, recent_event_item),
                class_name="flex flex-col gap-1",
            ),
            class_name=rx.cond(
                AppState.is_dark,
                "p-4 rounded-xl bg-slate-800 border border-slate-700 shadow-sm h-full",
                "p-4 rounded-xl bg-white border border-gray-200 shadow-sm h-full",
            ),
        ),
    )


def quick_action_button(label: str, icon: str) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, class_name="w-5 h-5 mb-2 opacity-80"),
        rx.el.span(label, class_name="text-xs font-semibold"),
        class_name=rx.cond(
            AppState.is_dark,
            "flex flex-col items-center justify-center p-4 rounded-xl bg-slate-800 border border-slate-700 hover:border-teal-500/50 hover:bg-slate-700 text-slate-300 hover:text-white transition-all shadow-sm",
            "flex flex-col items-center justify-center p-4 rounded-xl bg-white border border-gray-200 hover:border-teal-500/50 hover:bg-gray-50 text-gray-600 hover:text-gray-900 transition-all shadow-sm",
        ),
    )


def global_dashboard() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Dashboard Overview",
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-2xl font-bold text-white",
                    "text-2xl font-bold text-gray-900",
                ),
            ),
            rx.el.p(
                "Monitor your infrastructure health and performance across all engines.",
                class_name=rx.cond(
                    AppState.is_dark, "text-slate-400 mt-1", "text-gray-500 mt-1"
                ),
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            summary_card("Total Engines", DashboardState.total_engines, "server"),
            summary_card(
                "Active Clusters",
                DashboardState.total_clusters,
                "database",
                "All systems operational",
                "text-emerald-500",
            ),
            summary_card(
                "Total Nodes",
                DashboardState.total_nodes,
                "hard-drive",
                "+12 this week",
                "text-emerald-500",
            ),
            summary_card(
                "Environment Issues",
                DashboardState.env_issues_count,
                "flag_triangle_right",
                "Needs attention",
                "text-amber-500",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.div(environment_heatmap(), class_name="lg:col-span-2"),
            rx.el.div(recent_events_list(), class_name="lg:col-span-1"),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8",
        ),
        rx.el.div(
            rx.el.h3(
                "Quick Actions",
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-lg font-semibold text-white mb-4",
                    "text-lg font-semibold text-gray-900 mb-4",
                ),
            ),
            rx.el.div(
                quick_action_button("Create Cluster", "circle_plus"),
                quick_action_button("Run Plan", "file-text"),
                quick_action_button("Run Apply", "circle_play"),
                quick_action_button("View Telemetry", "activity"),
                quick_action_button("Manage Plugins", "box"),
                quick_action_button("System Logs", "terminal"),
                class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4",
            ),
        ),
    )