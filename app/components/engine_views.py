import reflex as rx
from app.states.app_state import AppState
from app.states.engine_state import EngineState


def status_badge(status: str) -> rx.Component:
    return rx.el.span(
        status,
        class_name=rx.match(
            status,
            (
                "Healthy",
                "px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400",
            ),
            (
                "Warning",
                "px-2.5 py-0.5 rounded-full text-xs font-medium bg-amber-100 text-amber-800 dark:bg-amber-900/30 dark:text-amber-400",
            ),
            (
                "Critical",
                "px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400",
            ),
            "px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-400",
        ),
    )


def engine_row(engine: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.span(engine["name"], class_name="font-semibold block"),
                rx.el.span(
                    engine["description"],
                    class_name="text-xs text-gray-500 dark:text-slate-400 truncate max-w-xs",
                ),
                class_name="",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
            on_click=lambda: AppState.navigate(f"/engines/{engine['id']}"),
        ),
        rx.el.td(
            rx.el.span(engine["plugin_id"], class_name="font-mono text-xs"),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-slate-400",
        ),
        rx.el.td(
            engine["version"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-slate-400",
        ),
        rx.el.td(
            rx.el.span(engine["clusters"], class_name="font-semibold"),
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-900 dark:text-white",
        ),
        rx.el.td(
            engine["last_scan"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-slate-400",
        ),
        rx.el.td(
            status_badge(engine["status"]), class_name="px-6 py-4 whitespace-nowrap"
        ),
        rx.el.td(
            rx.el.button(
                "View Details",
                on_click=lambda: AppState.navigate(f"/engines/{engine['id']}"),
                class_name="text-teal-600 hover:text-teal-900 dark:text-teal-400 dark:hover:text-teal-300 text-sm font-medium",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "hover:bg-slate-800/50 transition-colors cursor-pointer border-b border-slate-700 last:border-0",
            "hover:bg-gray-50 transition-colors cursor-pointer border-b border-gray-200 last:border-0",
        ),
    )


def engines_table() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "Engine Name",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Plugin ID",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Version",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Clusters",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Last Scan",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Status",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th("", class_name="px-6 py-3 relative"),
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "bg-slate-800 text-slate-300",
                    "bg-gray-50 text-gray-500",
                ),
            ),
            rx.el.tbody(
                rx.foreach(EngineState.engines, engine_row),
                class_name=rx.cond(
                    AppState.is_dark,
                    "bg-slate-900 divide-y divide-slate-800",
                    "bg-white divide-y divide-gray-200",
                ),
            ),
            class_name="min-w-full divide-y divide-gray-200 dark:divide-slate-700",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "overflow-hidden rounded-xl border border-slate-700 shadow-sm",
            "overflow-hidden rounded-xl border border-gray-200 shadow-sm",
        ),
    )


def engines_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Registered Engines",
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-2xl font-bold text-white",
                    "text-2xl font-bold text-gray-900",
                ),
            ),
            rx.el.p(
                "Manage your database and infrastructure engines.",
                class_name=rx.cond(
                    AppState.is_dark, "text-slate-400 mt-1", "text-gray-500 mt-1"
                ),
            ),
            class_name="mb-8",
        ),
        engines_table(),
    )


def engine_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    EngineState.current_engine["name"],
                    class_name=rx.cond(
                        AppState.is_dark,
                        "text-3xl font-bold text-white",
                        "text-3xl font-bold text-gray-900",
                    ),
                ),
                rx.el.div(
                    rx.el.span(
                        EngineState.current_engine["plugin_id"],
                        class_name="font-mono text-xs px-2 py-1 rounded bg-gray-100 dark:bg-slate-800 text-gray-600 dark:text-slate-400 mr-3",
                    ),
                    status_badge(EngineState.current_engine["status"]),
                    class_name="flex items-center mt-2",
                ),
                class_name="flex flex-col",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("plus", class_name="w-4 h-4 mr-2"),
                    "Create Cluster",
                    class_name="flex items-center px-4 py-2 rounded-lg bg-teal-600 hover:bg-teal-700 text-white font-medium transition-colors shadow-sm shadow-teal-900/20",
                ),
                class_name="flex items-center",
            ),
            class_name="flex justify-between items-start mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Total Clusters",
                    class_name="text-sm text-gray-500 dark:text-slate-400 mb-1",
                ),
                rx.el.span(
                    EngineState.current_engine["clusters"],
                    class_name="text-2xl font-bold text-gray-900 dark:text-white",
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "p-4 rounded-lg bg-slate-800 border border-slate-700",
                    "p-4 rounded-lg bg-white border border-gray-200",
                ),
            ),
            rx.el.div(
                rx.el.span(
                    "Total Nodes",
                    class_name="text-sm text-gray-500 dark:text-slate-400 mb-1",
                ),
                rx.el.span(
                    EngineState.current_engine["nodes"],
                    class_name="text-2xl font-bold text-gray-900 dark:text-white",
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "p-4 rounded-lg bg-slate-800 border border-slate-700",
                    "p-4 rounded-lg bg-white border border-gray-200",
                ),
            ),
            rx.el.div(
                rx.el.span(
                    "Version",
                    class_name="text-sm text-gray-500 dark:text-slate-400 mb-1",
                ),
                rx.el.span(
                    EngineState.current_engine["version"],
                    class_name="text-2xl font-bold text-gray-900 dark:text-white",
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "p-4 rounded-lg bg-slate-800 border border-slate-700",
                    "p-4 rounded-lg bg-white border border-gray-200",
                ),
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8",
        ),
    )


def tab_trigger(name: str) -> rx.Component:
    active = EngineState.current_tab == name
    return rx.el.button(
        name,
        on_click=lambda: EngineState.set_tab(name),
        class_name=rx.cond(
            active,
            rx.cond(
                AppState.is_dark,
                "px-4 py-2 text-sm font-medium text-teal-400 border-b-2 border-teal-400",
                "px-4 py-2 text-sm font-medium text-teal-600 border-b-2 border-teal-600",
            ),
            rx.cond(
                AppState.is_dark,
                "px-4 py-2 text-sm font-medium text-slate-400 hover:text-slate-200 border-b-2 border-transparent transition-colors",
                "px-4 py-2 text-sm font-medium text-gray-500 hover:text-gray-700 border-b-2 border-transparent transition-colors",
            ),
        ),
    )


def cluster_row(cluster: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            cluster["name"],
            class_name="px-6 py-4 text-sm font-medium text-gray-900 dark:text-white",
        ),
        rx.el.td(
            cluster["env"],
            class_name="px-6 py-4 text-sm text-gray-500 dark:text-slate-400",
        ),
        rx.el.td(
            cluster["topology"],
            class_name="px-6 py-4 text-sm text-gray-500 dark:text-slate-400",
        ),
        rx.el.td(
            cluster["nodes"],
            class_name="px-6 py-4 text-sm text-gray-500 dark:text-slate-400",
        ),
        rx.el.td(status_badge(cluster["health"]), class_name="px-6 py-4"),
        rx.el.td(
            cluster["last_op"],
            class_name="px-6 py-4 text-sm text-gray-500 dark:text-slate-400",
        ),
        rx.el.td(
            rx.el.button(
                "Manage",
                class_name="text-teal-600 hover:text-teal-900 dark:text-teal-400 dark:hover:text-teal-300 text-sm font-medium",
            ),
            class_name="px-6 py-4 text-right",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "border-b border-slate-700 last:border-0",
            "border-b border-gray-200 last:border-0",
        ),
    )


def clusters_tab_content() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "Cluster Name",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Environment",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Topology",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Nodes",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Health",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Last Operation",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th("", class_name="px-6 py-3"),
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "bg-slate-800 text-slate-300",
                    "bg-gray-50 text-gray-500",
                ),
            ),
            rx.el.tbody(
                rx.foreach(EngineState.clusters, cluster_row),
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
    )


def simple_placeholder_tab(message: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("construction", class_name="w-12 h-12 mb-4 opacity-50"),
            rx.el.h3(message, class_name="text-lg font-medium mb-2"),
            rx.el.p(
                "This view is under construction.", class_name="text-sm opacity-70"
            ),
            class_name="flex flex-col items-center justify-center h-64",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "rounded-xl border border-slate-700 border-dashed bg-slate-800/50",
            "rounded-xl border border-gray-300 border-dashed bg-gray-50",
        ),
    )


def engine_detail_page() -> rx.Component:
    return rx.el.div(
        engine_header(),
        rx.el.div(
            rx.el.nav(
                rx.foreach(EngineState.tabs, tab_trigger),
                class_name=rx.cond(
                    AppState.is_dark,
                    "flex gap-2 border-b border-slate-700 mb-6",
                    "flex gap-2 border-b border-gray-200 mb-6",
                ),
            )
        ),
        rx.match(
            EngineState.current_tab,
            ("Overview", simple_placeholder_tab("Engine Overview Dashboard")),
            ("Clusters", clusters_tab_content()),
            ("Telemetry", simple_placeholder_tab("Global Engine Telemetry")),
            ("Logs & Events", simple_placeholder_tab("Engine Log Stream")),
            ("Plugin Info", simple_placeholder_tab("Plugin Metadata & Config")),
            simple_placeholder_tab("Unknown Tab"),
        ),
    )