import reflex as rx
from app.states.app_state import AppState
from app.states.cluster_state import ClusterState

TOOLTIP_PROPS = {
    "content_style": {
        "background": "white",
        "borderColor": "#e2e8f0",
        "borderRadius": "0.5rem",
        "boxShadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        "fontFamily": "inherit",
        "fontSize": "0.875rem",
        "padding": "0.5rem",
    },
    "item_style": {"padding": "0", "color": "#475569"},
    "label_style": {"color": "#1e293b", "fontWeight": "600", "marginBottom": "0.25rem"},
    "separator": "",
}


def status_badge_lg(status: str) -> rx.Component:
    return rx.el.span(
        status,
        class_name=rx.match(
            status,
            (
                "Healthy",
                "px-3 py-1 rounded-full text-sm font-medium bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800",
            ),
            (
                "Warning",
                "px-3 py-1 rounded-full text-sm font-medium bg-amber-100 text-amber-800 dark:bg-amber-900/30 dark:text-amber-400 border border-amber-200 dark:border-amber-800",
            ),
            (
                "Critical",
                "px-3 py-1 rounded-full text-sm font-medium bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400 border border-red-200 dark:border-red-800",
            ),
            "px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-400",
        ),
    )


def topology_node(role: str, ip: str, status: str) -> rx.Component:
    is_master = role == "master"
    return rx.el.div(
        rx.el.div(
            rx.icon(
                "database",
                class_name=f"w-6 h-6 mb-1 {rx.cond(status == 'Healthy', 'text-emerald-500', 'text-red-500')}",
            ),
            rx.el.span(
                role.upper(),
                class_name="text-[10px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400",
            ),
            rx.el.span(
                ip,
                class_name="text-xs font-mono font-medium text-gray-900 dark:text-white",
            ),
            class_name="flex flex-col items-center",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            f"w-28 p-3 rounded-xl border-2 {rx.cond(is_master, 'border-teal-500/50 bg-slate-800', 'border-slate-700 bg-slate-800/50')} shadow-sm flex flex-col items-center gap-1 relative z-10",
            f"w-28 p-3 rounded-xl border-2 {rx.cond(is_master, 'border-teal-500/50 bg-white', 'border-gray-200 bg-gray-50')} shadow-sm flex flex-col items-center gap-1 relative z-10",
        ),
    )


def topology_diagram() -> rx.Component:
    """Visualizes the cluster topology."""
    return rx.el.div(
        rx.el.h3(
            "Topology Map",
            class_name="text-sm font-semibold text-gray-900 dark:text-white mb-6",
        ),
        rx.el.div(
            rx.el.div(
                topology_node("master", "10.0.1.101", "Healthy"),
                class_name="flex justify-center mb-8 relative",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="absolute top-[-2rem] left-1/2 -translate-x-1/2 h-8 w-0.5 bg-gray-300 dark:bg-slate-600"
                ),
                rx.el.div(
                    class_name="absolute top-0 left-[20%] right-[20%] h-0.5 bg-gray-300 dark:bg-slate-600"
                ),
                rx.el.div(
                    rx.el.div(
                        class_name="absolute top-0 left-[20%] h-4 w-0.5 bg-gray-300 dark:bg-slate-600"
                    ),
                    rx.el.div(
                        class_name="absolute top-0 right-[20%] h-4 w-0.5 bg-gray-300 dark:bg-slate-600"
                    ),
                ),
                class_name="relative h-4 w-full mb-2",
            ),
            rx.el.div(
                topology_node("replica", "10.0.1.102", "Healthy"),
                topology_node("replica", "10.0.1.103", "Healthy"),
                class_name="flex justify-center gap-16",
            ),
            class_name="flex flex-col items-center py-8",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "p-6 rounded-xl bg-slate-800/50 border border-slate-700",
            "p-6 rounded-xl bg-white border border-gray-200",
        ),
    )


def overview_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "Overall Health",
                            class_name="text-sm text-gray-500 dark:text-slate-400",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "100%",
                                class_name="text-2xl font-bold text-gray-900 dark:text-white",
                            ),
                            rx.el.span(
                                "Uptime",
                                class_name="text-xs font-medium text-emerald-500 ml-2",
                            ),
                            class_name="flex items-baseline",
                        ),
                        class_name=rx.cond(
                            AppState.is_dark,
                            "p-4 rounded-xl bg-slate-800 border border-slate-700",
                            "p-4 rounded-xl bg-white border border-gray-200",
                        ),
                    ),
                    rx.el.div(
                        rx.el.span(
                            "Active Connections",
                            class_name="text-sm text-gray-500 dark:text-slate-400",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "1,248",
                                class_name="text-2xl font-bold text-gray-900 dark:text-white",
                            ),
                            rx.el.span(
                                "+12%",
                                class_name="text-xs font-medium text-emerald-500 ml-2",
                            ),
                            class_name="flex items-baseline",
                        ),
                        class_name=rx.cond(
                            AppState.is_dark,
                            "p-4 rounded-xl bg-slate-800 border border-slate-700",
                            "p-4 rounded-xl bg-white border border-gray-200",
                        ),
                    ),
                    rx.el.div(
                        rx.el.span(
                            "Ops / Sec",
                            class_name="text-sm text-gray-500 dark:text-slate-400",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "45.2k",
                                class_name="text-2xl font-bold text-gray-900 dark:text-white",
                            ),
                            rx.el.span(
                                "stable",
                                class_name="text-xs font-medium text-gray-500 ml-2",
                            ),
                            class_name="flex items-baseline",
                        ),
                        class_name=rx.cond(
                            AppState.is_dark,
                            "p-4 rounded-xl bg-slate-800 border border-slate-700",
                            "p-4 rounded-xl bg-white border border-gray-200",
                        ),
                    ),
                    class_name="grid grid-cols-3 gap-4 mb-6",
                ),
                topology_diagram(),
                class_name="flex flex-col",
            ),
            rx.el.div(
                rx.cond(
                    ClusterState.cluster_info["air_gapped"],
                    rx.el.div(
                        rx.icon("shield-alert", class_name="w-5 h-5 text-amber-600"),
                        rx.el.div(
                            rx.el.span(
                                "Air-Gapped Environment",
                                class_name="block text-sm font-semibold text-amber-800 dark:text-amber-200",
                            ),
                            rx.el.span(
                                "External connectivity is disabled. Updates must be sideloaded.",
                                class_name="text-xs text-amber-700 dark:text-amber-300/80",
                            ),
                        ),
                        class_name="p-4 rounded-xl bg-amber-50 dark:bg-amber-900/20 border border-amber-200 dark:border-amber-800 flex gap-3 items-start mb-4",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Health Gates",
                        class_name="text-sm font-semibold text-gray-900 dark:text-white mb-4",
                    ),
                    rx.el.div(
                        rx.foreach(
                            ClusterState.health_checks,
                            lambda check: rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        rx.match(
                                            check["status"],
                                            ("Pass", "check-circle"),
                                            ("Warning", "alert-triangle"),
                                            "x-circle",
                                        ),
                                        class_name=rx.match(
                                            check["status"],
                                            ("Pass", "w-4 h-4 text-emerald-500"),
                                            ("Warning", "w-4 h-4 text-amber-500"),
                                            "w-4 h-4 text-red-500",
                                        ),
                                    ),
                                    rx.el.span(
                                        check["name"],
                                        class_name="text-sm font-medium text-gray-700 dark:text-slate-300",
                                    ),
                                    class_name="flex items-center gap-2",
                                ),
                                rx.el.span(
                                    check["message"],
                                    class_name="text-xs text-gray-500 dark:text-slate-500 ml-6",
                                ),
                                class_name="flex flex-col gap-0.5 pb-3 border-b border-gray-100 dark:border-slate-700 last:border-0",
                            ),
                        ),
                        class_name="flex flex-col gap-3",
                    ),
                    class_name=rx.cond(
                        AppState.is_dark,
                        "p-6 rounded-xl bg-slate-800 border border-slate-700",
                        "p-6 rounded-xl bg-white border border-gray-200",
                    ),
                ),
                class_name="flex flex-col",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-8",
        )
    )


def nodes_tab() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "Node Host",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Role",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Version",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Health",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Latency",
                        class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                    ),
                    rx.el.th(
                        "Lag",
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
                rx.foreach(
                    ClusterState.nodes,
                    lambda node: rx.el.tr(
                        rx.el.td(
                            rx.el.div(
                                rx.el.span(
                                    node["id"],
                                    class_name="block font-medium text-gray-900 dark:text-white",
                                ),
                                rx.el.span(
                                    node["host"],
                                    class_name="block text-xs text-gray-500 font-mono",
                                ),
                            ),
                            class_name="px-6 py-4",
                        ),
                        rx.el.td(
                            rx.el.span(
                                node["role"],
                                class_name="px-2 py-1 rounded text-xs font-medium bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-300 uppercase",
                            ),
                            class_name="px-6 py-4",
                        ),
                        rx.el.td(
                            node["version"],
                            class_name="px-6 py-4 text-sm text-gray-500 dark:text-slate-400",
                        ),
                        rx.el.td(
                            rx.el.div(
                                rx.el.div(
                                    class_name="w-2 h-2 rounded-full bg-emerald-500 mr-2"
                                ),
                                "Healthy",
                                class_name="flex items-center text-sm text-emerald-600 dark:text-emerald-400 font-medium",
                            ),
                            class_name="px-6 py-4",
                        ),
                        rx.el.td(
                            node["latency"],
                            class_name="px-6 py-4 text-sm font-mono text-gray-500 dark:text-slate-400",
                        ),
                        rx.el.td(
                            node["lag"],
                            class_name="px-6 py-4 text-sm font-mono text-gray-500 dark:text-slate-400",
                        ),
                        rx.el.td(
                            rx.el.div(
                                rx.el.button(
                                    "SSH",
                                    class_name="p-1.5 rounded hover:bg-gray-100 dark:hover:bg-slate-700 text-gray-500 dark:text-slate-400",
                                ),
                                rx.el.button(
                                    rx.icon("activity", class_name="w-4 h-4"),
                                    class_name="p-1.5 rounded hover:bg-gray-100 dark:hover:bg-slate-700 text-gray-500 dark:text-slate-400",
                                ),
                                class_name="flex items-center gap-2 justify-end",
                            ),
                            class_name="px-6 py-4",
                        ),
                        class_name=rx.cond(
                            AppState.is_dark,
                            "border-b border-slate-800 last:border-0",
                            "border-b border-gray-200 last:border-0",
                        ),
                    ),
                ),
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


def plan_apply_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Infrastructure Plan",
                        class_name="text-lg font-semibold text-gray-900 dark:text-white",
                    ),
                    rx.el.p(
                        "Review pending changes before applying.",
                        class_name="text-sm text-gray-500",
                    ),
                ),
                rx.el.button(
                    rx.cond(
                        ClusterState.is_applying,
                        rx.el.span("Applying...", class_name="flex items-center gap-2"),
                        rx.el.span(
                            "Run Apply",
                            class_name="flex items-center gap-2",
                            on_click=ClusterState.run_apply,
                        ),
                    ),
                    disabled=ClusterState.is_applying,
                    class_name="px-4 py-2 rounded-lg bg-teal-600 hover:bg-teal-700 disabled:opacity-50 disabled:cursor-not-allowed text-white font-medium transition-colors shadow-sm",
                ),
                class_name="flex justify-between items-center mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "Last Plan Output",
                            class_name="text-xs font-semibold uppercase tracking-wider text-gray-500 mb-2 block",
                        ),
                        rx.el.pre(
                            ClusterState.plan_output,
                            class_name="font-mono text-xs p-4 rounded-lg bg-gray-900 text-gray-300 overflow-x-auto whitespace-pre-wrap h-64",
                        ),
                        class_name="mb-8",
                    ),
                    rx.cond(
                        ClusterState.is_applying
                        | (ClusterState.apply_logs.length() > 0),
                        rx.el.div(
                            rx.el.div(
                                rx.el.span(
                                    "Apply Progress",
                                    class_name="text-xs font-semibold uppercase tracking-wider text-gray-500 mb-2 block",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        class_name="h-full bg-teal-500 transition-all duration-300 ease-out",
                                        style={
                                            "width": f"{ClusterState.apply_progress}%"
                                        },
                                    ),
                                    class_name="w-full h-1.5 bg-gray-200 dark:bg-slate-700 rounded-full overflow-hidden mb-4",
                                ),
                            ),
                            rx.el.div(
                                rx.foreach(
                                    ClusterState.apply_logs,
                                    lambda log: rx.el.div(
                                        log,
                                        class_name="font-mono text-xs text-gray-300 py-0.5 border-l-2 border-teal-500/50 pl-2",
                                    ),
                                ),
                                class_name="p-4 rounded-lg bg-gray-900/95 overflow-y-auto max-h-64",
                            ),
                            class_name="animate-in fade-in slide-in-from-top-4 duration-500",
                        ),
                    ),
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "p-6 rounded-xl bg-slate-800 border border-slate-700",
                    "p-6 rounded-xl bg-white border border-gray-200",
                ),
            ),
            class_name="max-w-5xl mx-auto",
        )
    )


def telemetry_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Latency (ms)",
                    class_name="text-sm font-semibold text-gray-900 dark:text-white mb-4",
                ),
                rx.el.div(
                    rx.recharts.line_chart(
                        rx.recharts.cartesian_grid(
                            stroke_dasharray="3 3",
                            vertical=False,
                            class_name="opacity-25",
                        ),
                        rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                        rx.recharts.x_axis(data_key="time", hide=True),
                        rx.recharts.y_axis(
                            tick_size=0,
                            axis_line=False,
                            tick_line=False,
                            class_name="text-xs font-mono opacity-50",
                        ),
                        rx.recharts.line(
                            data_key="p99",
                            stroke="#f59e0b",
                            type_="monotone",
                            stroke_width=2,
                            dot=False,
                        ),
                        rx.recharts.line(
                            data_key="p50",
                            stroke="#10b981",
                            type_="monotone",
                            stroke_width=2,
                            dot=False,
                        ),
                        data=ClusterState.telemetry_latency,
                        width="100%",
                        height="100%",
                    ),
                    class_name="h-64 w-full",
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "p-6 rounded-xl bg-slate-800 border border-slate-700",
                    "p-6 rounded-xl bg-white border border-gray-200",
                ),
            ),
            rx.el.div(
                rx.el.h3(
                    "Memory Usage (MB)",
                    class_name="text-sm font-semibold text-gray-900 dark:text-white mb-4",
                ),
                rx.el.div(
                    rx.recharts.area_chart(
                        rx.recharts.cartesian_grid(
                            stroke_dasharray="3 3",
                            vertical=False,
                            class_name="opacity-25",
                        ),
                        rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                        rx.recharts.x_axis(data_key="time", hide=True),
                        rx.recharts.y_axis(
                            tick_size=0,
                            axis_line=False,
                            tick_line=False,
                            class_name="text-xs font-mono opacity-50",
                        ),
                        rx.recharts.area(
                            data_key="used",
                            stroke="#3b82f6",
                            fill="#3b82f6",
                            fill_opacity=0.1,
                            type_="monotone",
                        ),
                        data=ClusterState.telemetry_memory,
                        width="100%",
                        height="100%",
                    ),
                    class_name="h-64 w-full",
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "p-6 rounded-xl bg-slate-800 border border-slate-700",
                    "p-6 rounded-xl bg-white border border-gray-200",
                ),
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6",
        )
    )


def config_tab() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Cluster Configuration",
                    class_name="text-lg font-semibold text-gray-900 dark:text-white mb-1",
                ),
                rx.el.p(
                    "Edit the raw configuration for this cluster.",
                    class_name="text-sm text-gray-500",
                ),
            ),
            rx.el.div(
                rx.el.button(
                    "Reset",
                    class_name="px-3 py-1.5 text-sm font-medium text-gray-600 hover:text-gray-900 dark:text-slate-400 dark:hover:text-white transition-colors",
                ),
                rx.el.button(
                    "Validate",
                    on_click=ClusterState.validate_config,
                    class_name="px-3 py-1.5 text-sm font-medium text-teal-600 hover:text-teal-700 dark:text-teal-400 dark:hover:text-teal-300 transition-colors",
                ),
                rx.el.button(
                    "Save Changes",
                    on_click=ClusterState.save_config,
                    class_name="ml-2 px-4 py-2 rounded-lg bg-teal-600 hover:bg-teal-700 text-white text-sm font-medium transition-colors shadow-sm",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex justify-between items-end mb-6",
        ),
        rx.el.div(
            rx.el.textarea(
                default_value=ClusterState.config_yaml,
                class_name="w-full h-[500px] font-mono text-sm p-4 rounded-lg bg-gray-900 text-gray-300 focus:ring-2 focus:ring-teal-500/50 focus:outline-none resize-none leading-relaxed",
                spell_check=False,
            ),
            class_name=rx.cond(
                AppState.is_dark,
                "p-1 rounded-xl bg-slate-800 border border-slate-700",
                "p-1 rounded-xl bg-white border border-gray-200",
            ),
        ),
    )


def cluster_detail_header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.button(
                rx.icon("arrow-left", class_name="w-4 h-4 mr-1"),
                "Back to Engines",
                on_click=lambda: AppState.navigate("/engines"),
                class_name="flex items-center text-sm text-gray-500 hover:text-gray-900 dark:text-slate-400 dark:hover:text-white transition-colors mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        ClusterState.cluster_info["name"],
                        class_name="text-3xl font-bold text-gray-900 dark:text-white",
                    ),
                    rx.el.div(
                        rx.el.span(
                            ClusterState.cluster_info["engine"],
                            class_name="px-2 py-1 rounded bg-gray-100 dark:bg-slate-800 text-xs font-mono text-gray-600 dark:text-slate-400",
                        ),
                        status_badge_lg(ClusterState.cluster_info["health"]),
                        class_name="flex items-center gap-2 mt-2",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "Environment",
                            class_name="text-xs text-gray-500 dark:text-slate-400 uppercase tracking-wider",
                        ),
                        rx.el.span(
                            ClusterState.cluster_info["environment"],
                            class_name="font-medium text-gray-900 dark:text-white",
                        ),
                        class_name="flex flex-col items-end",
                    ),
                    rx.el.div(class_name="w-px h-8 bg-gray-200 dark:bg-slate-700 mx-6"),
                    rx.el.div(
                        rx.el.span(
                            "Topology",
                            class_name="text-xs text-gray-500 dark:text-slate-400 uppercase tracking-wider",
                        ),
                        rx.el.span(
                            ClusterState.cluster_info["topology"],
                            class_name="font-medium text-gray-900 dark:text-white",
                        ),
                        class_name="flex flex-col items-end",
                    ),
                    rx.el.div(class_name="w-px h-8 bg-gray-200 dark:bg-slate-700 mx-6"),
                    rx.el.div(
                        rx.el.span(
                            "Version",
                            class_name="text-xs text-gray-500 dark:text-slate-400 uppercase tracking-wider",
                        ),
                        rx.el.span(
                            ClusterState.cluster_info["version"],
                            class_name="font-medium text-gray-900 dark:text-white",
                        ),
                        class_name="flex flex-col items-end",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex justify-between items-start",
            ),
            class_name="mb-8",
        ),
        rx.el.nav(
            rx.foreach(
                ["Overview", "Nodes", "Plan & Apply", "Telemetry", "Config", "Logs"],
                lambda tab: rx.el.button(
                    tab,
                    on_click=lambda: ClusterState.set_tab(tab),
                    class_name=rx.cond(
                        ClusterState.current_tab == tab,
                        "px-4 py-2 text-sm font-medium text-teal-600 dark:text-teal-400 border-b-2 border-teal-600 dark:border-teal-400",
                        "px-4 py-2 text-sm font-medium text-gray-500 hover:text-gray-700 dark:text-slate-400 dark:hover:text-slate-200 border-b-2 border-transparent transition-colors",
                    ),
                ),
            ),
            class_name="flex gap-2 border-b border-gray-200 dark:border-slate-700 mb-8",
        ),
    )


def cluster_detail_page() -> rx.Component:
    return rx.el.div(
        cluster_detail_header(),
        rx.match(
            ClusterState.current_tab,
            ("Overview", overview_tab()),
            ("Nodes", nodes_tab()),
            ("Plan & Apply", plan_apply_tab()),
            ("Telemetry", telemetry_tab()),
            ("Config", config_tab()),
            rx.el.div("Content for this tab is under construction."),
        ),
    )