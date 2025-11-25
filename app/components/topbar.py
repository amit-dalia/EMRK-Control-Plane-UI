import reflex as rx
from app.states.app_state import AppState


def topbar() -> rx.Component:
    """The top navigation bar containing filters and user controls."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Environment:",
                    class_name=rx.cond(
                        AppState.is_dark,
                        "text-xs text-slate-400 font-medium mr-2",
                        "text-xs text-gray-500 font-medium mr-2",
                    ),
                ),
                rx.el.select(
                    rx.foreach(
                        AppState.environments, lambda env: rx.el.option(env, value=env)
                    ),
                    value=AppState.current_env,
                    on_change=AppState.set_env,
                    class_name=rx.cond(
                        AppState.is_dark,
                        "bg-slate-800 text-sm font-medium text-white border-slate-700 rounded-md px-3 py-1.5 focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 outline-none cursor-pointer",
                        "bg-white text-sm font-medium text-gray-900 border-gray-200 border rounded-md px-3 py-1.5 focus:ring-2 focus:ring-teal-500/20 focus:border-teal-500 outline-none cursor-pointer",
                    ),
                ),
                class_name="flex items-center",
            ),
            rx.el.div(
                class_name=rx.cond(
                    AppState.is_dark,
                    "h-6 w-px bg-slate-700 mx-4",
                    "h-6 w-px bg-gray-200 mx-4",
                )
            ),
            rx.el.div(
                rx.icon(
                    "filter",
                    class_name=rx.cond(
                        AppState.is_dark,
                        "w-4 h-4 text-slate-400 mr-2",
                        "w-4 h-4 text-gray-400 mr-2",
                    ),
                ),
                rx.el.select(
                    rx.foreach(
                        AppState.engines,
                        lambda engine: rx.el.option(engine, value=engine),
                    ),
                    value=AppState.selected_engine,
                    on_change=AppState.set_engine,
                    class_name=rx.cond(
                        AppState.is_dark,
                        "bg-transparent text-sm text-slate-300 font-medium outline-none cursor-pointer hover:text-white transition-colors",
                        "bg-transparent text-sm text-gray-600 font-medium outline-none cursor-pointer hover:text-gray-900 transition-colors",
                    ),
                ),
                class_name="flex items-center",
            ),
            class_name="flex items-center",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    class_name=rx.cond(
                        AppState.is_dark,
                        "w-4 h-4 text-slate-500",
                        "w-4 h-4 text-gray-400",
                    ),
                ),
                rx.el.input(
                    placeholder="Search resources...",
                    class_name=rx.cond(
                        AppState.is_dark,
                        "bg-transparent border-none text-sm text-white placeholder-slate-500 focus:ring-0 w-48",
                        "bg-transparent border-none text-sm text-gray-900 placeholder-gray-400 focus:ring-0 w-48",
                    ),
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "flex items-center bg-slate-800 rounded-full px-3 py-1.5 mr-4 border border-slate-700",
                    "flex items-center bg-gray-100 rounded-full px-3 py-1.5 mr-4 border border-transparent",
                ),
            ),
            rx.el.button(
                rx.cond(
                    AppState.is_dark,
                    rx.icon("sun", class_name="w-5 h-5 text-amber-400"),
                    rx.icon("moon", class_name="w-5 h-5 text-slate-600"),
                ),
                on_click=AppState.toggle_theme,
                class_name=rx.cond(
                    AppState.is_dark,
                    "p-2 rounded-full hover:bg-slate-800 transition-colors mr-2",
                    "p-2 rounded-full hover:bg-gray-100 transition-colors mr-2",
                ),
            ),
            rx.el.button(
                rx.el.div(
                    rx.icon(
                        "bell",
                        class_name=rx.cond(
                            AppState.is_dark,
                            "w-5 h-5 text-slate-400",
                            "w-5 h-5 text-gray-500",
                        ),
                    ),
                    rx.el.span(
                        class_name="absolute top-2 right-2 w-2 h-2 bg-red-500 rounded-full border-2 border-white dark:border-slate-900"
                    ),
                    class_name="relative",
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "p-2 rounded-full hover:bg-slate-800 transition-colors mr-4",
                    "p-2 rounded-full hover:bg-gray-100 transition-colors mr-4",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span("JS", class_name="text-xs font-bold text-white"),
                    class_name="w-8 h-8 rounded-full bg-gradient-to-br from-teal-500 to-emerald-600 flex items-center justify-center shadow-md",
                ),
                rx.el.div(
                    rx.el.span(
                        "John Smith",
                        class_name=rx.cond(
                            AppState.is_dark,
                            "text-sm font-medium text-white block leading-none",
                            "text-sm font-medium text-gray-900 block leading-none",
                        ),
                    ),
                    rx.el.span(
                        "DevOps Lead",
                        class_name=rx.cond(
                            AppState.is_dark,
                            "text-xs text-slate-500",
                            "text-xs text-gray-500",
                        ),
                    ),
                    class_name="flex flex-col ml-2",
                ),
                rx.icon(
                    "chevron-down",
                    class_name=rx.cond(
                        AppState.is_dark,
                        "w-4 h-4 text-slate-500 ml-2",
                        "w-4 h-4 text-gray-400 ml-2",
                    ),
                ),
                class_name=rx.cond(
                    AppState.is_dark,
                    "flex items-center pl-2 border-l border-slate-700 cursor-pointer hover:opacity-80",
                    "flex items-center pl-2 border-l border-gray-200 cursor-pointer hover:opacity-80",
                ),
            ),
            class_name="flex items-center",
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "h-16 flex items-center justify-between px-6 border-b border-slate-800 bg-slate-900 transition-colors duration-300",
            "h-16 flex items-center justify-between px-6 border-b border-gray-200 bg-white transition-colors duration-300",
        ),
    )