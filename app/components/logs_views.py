import reflex as rx
from app.states.app_state import AppState
from app.states.logs_state import LogsState


def log_severity_badge(severity: str) -> rx.Component:
    return rx.el.span(
        severity,
        class_name=rx.match(
            severity,
            (
                "Info",
                "px-2 py-0.5 rounded text-xs font-medium bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400",
            ),
            (
                "Warning",
                "px-2 py-0.5 rounded text-xs font-medium bg-amber-100 text-amber-800 dark:bg-amber-900/30 dark:text-amber-400",
            ),
            (
                "Error",
                "px-2 py-0.5 rounded text-xs font-medium bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400",
            ),
            (
                "Success",
                "px-2 py-0.5 rounded text-xs font-medium bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400",
            ),
            "px-2 py-0.5 rounded text-xs font-medium bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-400",
        ),
    )


def log_row(log: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            log["timestamp"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-mono text-gray-500 dark:text-slate-500",
        ),
        rx.el.td(
            rx.el.span(
                log["engine"],
                class_name="px-2 py-1 rounded bg-gray-100 dark:bg-slate-800 text-xs font-medium text-gray-600 dark:text-slate-400",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            log["cluster"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-900 dark:text-white",
        ),
        rx.el.td(
            log_severity_badge(log["severity"]),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            log["message"],
            class_name="px-6 py-4 text-sm text-gray-600 dark:text-slate-300 font-mono",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "border-b border-slate-800 hover:bg-slate-800/50 transition-colors",
            "border-b border-gray-200 hover:bg-gray-50 transition-colors",
        ),
    )


def logs_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "System Logs & Events",
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-2xl font-bold text-white",
                    "text-2xl font-bold text-gray-900",
                ),
            ),
            rx.el.p(
                "Search and filter through system-wide events and audit logs.",
                class_name=rx.cond(
                    AppState.is_dark, "text-slate-400 mt-1", "text-gray-500 mt-1"
                ),
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("search", class_name="w-4 h-4 text-gray-500 mr-2"),
                    rx.el.input(
                        placeholder="Search logs...",
                        on_change=LogsState.set_search,
                        class_name="bg-transparent border-none focus:ring-0 text-sm w-full",
                        default_value=LogsState.search_query,
                    ),
                    class_name=rx.cond(
                        AppState.is_dark,
                        "flex items-center flex-1 max-w-md bg-slate-800 border border-slate-700 rounded-md px-3 py-1.5 focus-within:ring-2 focus-within:ring-teal-500/50 mr-4",
                        "flex items-center flex-1 max-w-md bg-white border border-gray-200 rounded-md px-3 py-1.5 focus-within:ring-2 focus-within:ring-teal-500/20 mr-4",
                    ),
                ),
                rx.el.select(
                    rx.el.option("All Severities", value="All"),
                    rx.el.option("Info", value="Info"),
                    rx.el.option("Warning", value="Warning"),
                    rx.el.option("Error", value="Error"),
                    rx.el.option("Success", value="Success"),
                    value=LogsState.severity_filter,
                    on_change=LogsState.set_severity,
                    class_name=rx.cond(
                        AppState.is_dark,
                        "bg-slate-800 text-sm font-medium text-white border-slate-700 rounded-md px-3 py-1.5 focus:ring-2 focus:ring-teal-500/50 outline-none",
                        "bg-white text-sm font-medium text-gray-900 border-gray-200 border rounded-md px-3 py-1.5 focus:ring-2 focus:ring-teal-500/20 outline-none",
                    ),
                ),
                class_name="flex mb-6",
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Timestamp",
                                class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                            ),
                            rx.el.th(
                                "Engine",
                                class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                            ),
                            rx.el.th(
                                "Cluster",
                                class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                            ),
                            rx.el.th(
                                "Severity",
                                class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                            ),
                            rx.el.th(
                                "Message",
                                class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                            ),
                        ),
                        class_name=rx.cond(
                            AppState.is_dark,
                            "bg-slate-800 text-slate-300",
                            "bg-gray-50 text-gray-500",
                        ),
                    ),
                    rx.el.tbody(
                        rx.foreach(LogsState.filtered_logs, log_row),
                        class_name=rx.cond(
                            AppState.is_dark,
                            "bg-slate-900 divide-y divide-slate-800",
                            "bg-white divide-y divide-gray-200",
                        ),
                    ),
                    class_name="min-w-full",
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "overflow-hidden rounded-xl border border-slate-700 shadow-sm",
                    "overflow-hidden rounded-xl border border-gray-200 shadow-sm",
                ),
            ),
        ),
    )