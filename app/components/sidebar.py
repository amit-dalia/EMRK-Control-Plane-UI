import reflex as rx
from app.states.app_state import AppState


def sidebar_item(item: dict) -> rx.Component:
    """Render a single sidebar navigation item."""
    active = AppState.current_path == item["path"]
    return rx.el.button(
        rx.icon(
            item["icon"],
            class_name=rx.cond(
                active,
                "w-5 h-5 text-teal-500",
                rx.cond(
                    AppState.is_dark, "w-5 h-5 text-slate-400", "w-5 h-5 text-gray-500"
                ),
            ),
        ),
        rx.el.span(
            item["label"],
            class_name=rx.cond(
                active,
                "font-medium text-teal-500",
                rx.cond(
                    AppState.is_dark,
                    "font-medium text-slate-300 group-hover:text-white",
                    "font-medium text-gray-600 group-hover:text-gray-900",
                ),
            ),
        ),
        on_click=lambda: AppState.navigate(item["path"]),
        class_name=rx.cond(
            active,
            rx.cond(
                AppState.is_dark,
                "flex items-center gap-3 px-3 py-2.5 rounded-lg bg-slate-800 border-r-2 border-teal-500 transition-all w-full text-left",
                "flex items-center gap-3 px-3 py-2.5 rounded-lg bg-teal-50 border-r-2 border-teal-500 transition-all w-full text-left",
            ),
            "flex items-center gap-3 px-3 py-2.5 rounded-lg hover:bg-opacity-50 transition-all w-full text-left group hover:bg-gray-100/5",
        ),
    )


def sidebar() -> rx.Component:
    """The main sidebar component."""
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon("hexagon", class_name="w-8 h-8 text-teal-500 fill-current"),
                rx.el.div(
                    rx.el.h1(
                        "EMRK",
                        class_name=rx.cond(
                            AppState.is_dark,
                            "text-xl font-bold text-white tracking-tight",
                            "text-xl font-bold text-gray-900 tracking-tight",
                        ),
                    ),
                    rx.el.span(
                        "Manager",
                        class_name="text-xs font-medium text-teal-500 uppercase tracking-wider",
                    ),
                    class_name="flex flex-col leading-none",
                ),
                class_name="flex items-center gap-3",
            ),
            class_name=rx.cond(
                AppState.is_dark,
                "h-16 flex items-center px-6 border-b border-slate-800",
                "h-16 flex items-center px-6 border-b border-gray-100",
            ),
        ),
        rx.el.nav(
            rx.el.div(
                rx.el.span(
                    "MAIN MENU",
                    class_name=rx.cond(
                        AppState.is_dark,
                        "text-xs font-semibold text-slate-500 uppercase tracking-wider mb-4 block",
                        "text-xs font-semibold text-gray-400 uppercase tracking-wider mb-4 block",
                    ),
                ),
                rx.foreach(AppState.menu_items, sidebar_item),
                class_name="flex flex-col gap-1",
            ),
            class_name="flex-1 overflow-y-auto p-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span("v2.4.0", class_name="text-xs font-mono opacity-70"),
                    rx.el.span("•", class_name="mx-2 opacity-50"),
                    rx.el.span(
                        "Stable", class_name="text-xs text-teal-500 font-medium"
                    ),
                    class_name=rx.cond(
                        AppState.is_dark, "text-slate-500", "text-gray-400"
                    ),
                ),
                class_name="px-6 py-4",
            ),
            class_name=rx.cond(
                AppState.is_dark,
                "border-t border-slate-800",
                "border-t border-gray-100",
            ),
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "w-64 flex flex-col h-full bg-slate-900 border-r border-slate-800 transition-colors duration-300 flex-shrink-0",
            "w-64 flex flex-col h-full bg-white border-r border-gray-200 transition-colors duration-300 flex-shrink-0",
        ),
    )