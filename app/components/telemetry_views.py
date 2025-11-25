import reflex as rx
from app.states.app_state import AppState
from app.states.telemetry_state import TelemetryState

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


def stat_card(
    title: str, value: str, change: str, is_good: bool = True
) -> rx.Component:
    color = "text-emerald-500" if is_good else "text-red-500"
    return rx.el.div(
        rx.el.div(
            rx.el.span(title, class_name="text-sm font-medium opacity-70"),
            class_name="mb-2",
        ),
        rx.el.div(
            rx.el.span(value, class_name="text-2xl font-bold"),
            rx.el.span(change, class_name=f"text-xs font-medium ml-2 {color}"),
            class_name="flex items-baseline",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "p-6 rounded-xl bg-slate-800 border border-slate-700 shadow-sm",
            "p-6 rounded-xl bg-white border border-gray-200 shadow-sm",
        ),
    )


def telemetry_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Global Telemetry",
                    class_name=rx.cond(
                        AppState.is_dark,
                        "text-2xl font-bold text-white",
                        "text-2xl font-bold text-gray-900",
                    ),
                ),
                rx.el.div(
                    rx.el.select(
                        rx.el.option("Last Hour", value="1h"),
                        rx.el.option("Last 24 Hours", value="24h"),
                        rx.el.option("Last 7 Days", value="7d"),
                        value=TelemetryState.time_range,
                        on_change=TelemetryState.set_time_range,
                        class_name=rx.cond(
                            AppState.is_dark,
                            "bg-slate-800 text-sm font-medium text-white border-slate-700 rounded-md px-3 py-1.5 focus:ring-2 focus:ring-teal-500/50 outline-none",
                            "bg-white text-sm font-medium text-gray-900 border-gray-200 border rounded-md px-3 py-1.5 focus:ring-2 focus:ring-teal-500/20 outline-none",
                        ),
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex justify-between items-center mb-8",
            ),
            rx.el.div(
                stat_card("Avg. Latency", "24ms", "-12%", True),
                stat_card("Failure Rate", "0.01%", "+0.002%", False),
                stat_card("Node Availability", "99.9%", "stable", True),
                stat_card("Total Operations", "14.5M", "+5%", True),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Latency by Engine (ms)",
                        class_name="text-lg font-semibold mb-4",
                    ),
                    rx.el.div(
                        rx.recharts.line_chart(
                            rx.recharts.cartesian_grid(
                                stroke_dasharray="3 3",
                                vertical=False,
                                class_name="opacity-25",
                            ),
                            rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                            rx.recharts.x_axis(data_key="time"),
                            rx.recharts.y_axis(
                                tick_size=0,
                                axis_line=False,
                                tick_line=False,
                                class_name="text-xs font-mono opacity-50",
                            ),
                            rx.recharts.line(
                                data_key="Redis",
                                stroke="#ef4444",
                                type_="monotone",
                                stroke_width=2,
                                dot=False,
                            ),
                            rx.recharts.line(
                                data_key="Kafka",
                                stroke="#f59e0b",
                                type_="monotone",
                                stroke_width=2,
                                dot=False,
                            ),
                            rx.recharts.line(
                                data_key="Postgres",
                                stroke="#3b82f6",
                                type_="monotone",
                                stroke_width=2,
                                dot=False,
                            ),
                            data=TelemetryState.latency_data,
                            width="100%",
                            height="100%",
                        ),
                        class_name="h-64 w-full",
                    ),
                    class_name=rx.cond(
                        AppState.is_dark,
                        "p-6 rounded-xl bg-slate-800 border border-slate-700 shadow-sm",
                        "p-6 rounded-xl bg-white border border-gray-200 shadow-sm",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Operations / Sec", class_name="text-lg font-semibold mb-4"
                    ),
                    rx.el.div(
                        rx.recharts.bar_chart(
                            rx.recharts.cartesian_grid(
                                stroke_dasharray="3 3",
                                vertical=False,
                                class_name="opacity-25",
                            ),
                            rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                            rx.recharts.x_axis(data_key="time"),
                            rx.recharts.y_axis(
                                tick_size=0,
                                axis_line=False,
                                tick_line=False,
                                class_name="text-xs font-mono opacity-50",
                            ),
                            rx.recharts.bar(
                                data_key="ops", fill="#10b981", radius=[4, 4, 0, 0]
                            ),
                            data=TelemetryState.ops_data,
                            width="100%",
                            height="100%",
                        ),
                        class_name="h-64 w-full",
                    ),
                    class_name=rx.cond(
                        AppState.is_dark,
                        "p-6 rounded-xl bg-slate-800 border border-slate-700 shadow-sm",
                        "p-6 rounded-xl bg-white border border-gray-200 shadow-sm",
                    ),
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8",
            ),
            rx.el.div(
                rx.el.h3(
                    "Error Count by Cluster", class_name="text-lg font-semibold mb-4"
                ),
                rx.el.div(
                    rx.recharts.bar_chart(
                        rx.recharts.cartesian_grid(
                            stroke_dasharray="3 3",
                            vertical=False,
                            class_name="opacity-25",
                        ),
                        rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                        rx.recharts.x_axis(data_key="cluster"),
                        rx.recharts.y_axis(
                            tick_size=0,
                            axis_line=False,
                            tick_line=False,
                            class_name="text-xs font-mono opacity-50",
                        ),
                        rx.recharts.bar(
                            data_key="errors", fill="#ef4444", radius=[4, 4, 0, 0]
                        ),
                        data=TelemetryState.error_rate_data,
                        layout="vertical",
                        width="100%",
                        height="100%",
                    ),
                    class_name="h-64 w-full",
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "p-6 rounded-xl bg-slate-800 border border-slate-700 shadow-sm",
                    "p-6 rounded-xl bg-white border border-gray-200 shadow-sm",
                ),
            ),
        )
    )