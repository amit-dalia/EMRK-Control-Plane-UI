import reflex as rx
from app.states.app_state import AppState
from app.states.jobs_state import JobsState


def job_status_badge(status: str) -> rx.Component:
    return rx.el.span(
        status,
        class_name=rx.match(
            status,
            (
                "Success",
                "px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800 dark:bg-emerald-900/30 dark:text-emerald-400",
            ),
            (
                "Failed",
                "px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400",
            ),
            (
                "Running",
                "px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400",
            ),
            "px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-400",
        ),
    )


def job_row(job: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.span(job["id"], class_name="font-mono text-xs font-medium"),
            class_name="px-6 py-4 whitespace-nowrap text-gray-900 dark:text-white",
        ),
        rx.el.td(
            rx.el.div(
                rx.icon(
                    rx.match(
                        job["type"],
                        ("Apply", "play-circle"),
                        ("Plan", "file-text"),
                        ("Upgrade", "arrow-up-circle"),
                        "activity",
                    ),
                    class_name="w-4 h-4 mr-2 opacity-70",
                ),
                job["type"],
                class_name="flex items-center text-sm text-gray-600 dark:text-slate-300",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            job["engine"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-600 dark:text-slate-400",
        ),
        rx.el.td(
            job["cluster"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 dark:text-white",
        ),
        rx.el.td(
            job["env"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-600 dark:text-slate-400",
        ),
        rx.el.td(
            job["started"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-slate-500",
        ),
        rx.el.td(
            job["duration"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-mono text-gray-500 dark:text-slate-500",
        ),
        rx.el.td(
            job_status_badge(job["status"]), class_name="px-6 py-4 whitespace-nowrap"
        ),
        rx.el.td(
            rx.el.button(
                "Details",
                on_click=lambda: JobsState.select_job(job),
                class_name="text-teal-600 hover:text-teal-900 dark:text-teal-400 dark:hover:text-teal-300 text-sm font-medium",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "border-b border-slate-800 hover:bg-slate-800/50 transition-colors",
            "border-b border-gray-200 hover:bg-gray-50 transition-colors",
        ),
    )


def job_detail_modal() -> rx.Component:
    return rx.cond(
        JobsState.selected_job,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            f"Job Details: {JobsState.selected_job['id']}",
                            class_name="text-lg font-semibold text-gray-900 dark:text-white",
                        ),
                        rx.el.button(
                            rx.icon("x", class_name="w-5 h-5"),
                            on_click=JobsState.close_modal,
                            class_name="text-gray-500 hover:text-gray-700 dark:text-slate-400 dark:hover:text-white",
                        ),
                        class_name="flex justify-between items-center mb-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                "Type", class_name="text-xs text-gray-500 uppercase"
                            ),
                            rx.el.span(
                                JobsState.selected_job["type"], class_name="font-medium"
                            ),
                            class_name="flex flex-col",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "Cluster", class_name="text-xs text-gray-500 uppercase"
                            ),
                            rx.el.span(
                                JobsState.selected_job["cluster"],
                                class_name="font-medium",
                            ),
                            class_name="flex flex-col",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "Status", class_name="text-xs text-gray-500 uppercase"
                            ),
                            job_status_badge(JobsState.selected_job["status"]),
                            class_name="flex flex-col items-start",
                        ),
                        class_name="grid grid-cols-3 gap-4 mb-6 p-4 bg-gray-50 dark:bg-slate-800/50 rounded-lg",
                    ),
                    rx.el.div(
                        rx.el.h4(
                            "Execution Logs", class_name="text-sm font-semibold mb-2"
                        ),
                        rx.el.div(
                            rx.el.div(
                                "[10:23:45] Initializing job runner...",
                                class_name="text-xs font-mono text-gray-600 dark:text-slate-400 mb-1",
                            ),
                            rx.el.div(
                                "[10:23:46] Loading plugin context for engine: Redis",
                                class_name="text-xs font-mono text-gray-600 dark:text-slate-400 mb-1",
                            ),
                            rx.el.div(
                                "[10:23:48] Connecting to cluster cache-prod-useast...",
                                class_name="text-xs font-mono text-gray-600 dark:text-slate-400 mb-1",
                            ),
                            rx.el.div(
                                "[10:23:55] Operation completed successfully.",
                                class_name="text-xs font-mono text-emerald-600 dark:text-emerald-400 mb-1",
                            ),
                            class_name="bg-gray-900 rounded-lg p-4 overflow-y-auto max-h-64",
                        ),
                    ),
                    class_name=rx.cond(
                        AppState.is_dark,
                        "bg-slate-900 rounded-xl shadow-xl border border-slate-700 p-6 max-w-2xl w-full m-4",
                        "bg-white rounded-xl shadow-xl border border-gray-200 p-6 max-w-2xl w-full m-4",
                    ),
                ),
                class_name="fixed inset-0 z-50 flex items-center justify-center pointer-events-none",
            ),
            rx.el.div(
                class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40",
                on_click=JobsState.close_modal,
            ),
            class_name="fixed inset-0 z-50 overflow-y-auto",
        ),
    )


def jobs_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Operations & Jobs",
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-2xl font-bold text-white",
                    "text-2xl font-bold text-gray-900",
                ),
            ),
            rx.el.p(
                "Monitor and audit all operations running across your infrastructure.",
                class_name=rx.cond(
                    AppState.is_dark, "text-slate-400 mt-1", "text-gray-500 mt-1"
                ),
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.select(
                    rx.el.option("All Types", value="All Types"),
                    rx.el.option("Apply", value="Apply"),
                    rx.el.option("Plan", value="Plan"),
                    rx.el.option("Upgrade", value="Upgrade"),
                    rx.el.option("Health Scan", value="Health Scan"),
                    value=JobsState.type_filter,
                    on_change=JobsState.set_type_filter,
                    class_name=rx.cond(
                        AppState.is_dark,
                        "bg-slate-800 text-sm font-medium text-white border-slate-700 rounded-md px-3 py-1.5 focus:ring-2 focus:ring-teal-500/50 outline-none",
                        "bg-white text-sm font-medium text-gray-900 border-gray-200 border rounded-md px-3 py-1.5 focus:ring-2 focus:ring-teal-500/20 outline-none",
                    ),
                ),
                rx.el.select(
                    rx.el.option("All Statuses", value="All Statuses"),
                    rx.el.option("Success", value="Success"),
                    rx.el.option("Failed", value="Failed"),
                    rx.el.option("Running", value="Running"),
                    value=JobsState.status_filter,
                    on_change=JobsState.set_status_filter,
                    class_name=rx.cond(
                        AppState.is_dark,
                        "bg-slate-800 text-sm font-medium text-white border-slate-700 rounded-md px-3 py-1.5 focus:ring-2 focus:ring-teal-500/50 outline-none ml-4",
                        "bg-white text-sm font-medium text-gray-900 border-gray-200 border rounded-md px-3 py-1.5 focus:ring-2 focus:ring-teal-500/20 outline-none ml-4",
                    ),
                ),
                class_name="flex mb-6",
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Job ID",
                                class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                            ),
                            rx.el.th(
                                "Type",
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
                                "Env",
                                class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                            ),
                            rx.el.th(
                                "Started",
                                class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                            ),
                            rx.el.th(
                                "Duration",
                                class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                            ),
                            rx.el.th(
                                "Status",
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
                        rx.foreach(JobsState.filtered_jobs, job_row),
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
        job_detail_modal(),
    )