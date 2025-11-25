import reflex as rx
from app.states.app_state import AppState
from app.components.sidebar import sidebar
from app.components.topbar import topbar


def layout(content: rx.Component) -> rx.Component:
    """The main application layout wrapper."""
    return rx.el.div(
        sidebar(),
        rx.el.div(
            topbar(),
            rx.el.main(content, class_name="flex-1 overflow-y-auto p-6"),
            class_name=rx.cond(
                AppState.is_dark,
                "flex-1 flex flex-col min-w-0 bg-slate-900/50",
                "flex-1 flex flex-col min-w-0 bg-gray-50",
            ),
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "flex h-screen w-full bg-slate-900 transition-colors duration-300 font-['Roboto'] selection:bg-teal-500/30",
            "flex h-screen w-full bg-gray-50 transition-colors duration-300 font-['Roboto'] selection:bg-teal-500/20",
        ),
    )