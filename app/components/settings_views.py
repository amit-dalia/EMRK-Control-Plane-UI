import reflex as rx
from app.states.app_state import AppState
from app.states.settings_state import SettingsState


def settings_section(
    title: str, description: str, content: rx.Component
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                title,
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-lg font-medium text-white",
                    "text-lg font-medium text-gray-900",
                ),
            ),
            rx.el.p(
                description,
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-sm text-slate-400 mt-1",
                    "text-sm text-gray-500 mt-1",
                ),
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            content,
            class_name=rx.cond(
                AppState.is_dark,
                "p-6 rounded-xl bg-slate-800 border border-slate-700 shadow-sm",
                "p-6 rounded-xl bg-white border border-gray-200 shadow-sm",
            ),
        ),
        class_name="mb-8",
    )


def api_config_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.label(
                "API Base URL", class_name="block text-sm font-medium mb-2 opacity-80"
            ),
            rx.el.input(
                default_value=SettingsState.api_url,
                class_name=rx.cond(
                    AppState.is_dark,
                    "w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded-lg focus:ring-2 focus:ring-teal-500/50 outline-none",
                    "w-full px-3 py-2 bg-white border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500/20 outline-none",
                ),
            ),
            class_name="mb-4",
        ),
        rx.el.div(
            rx.el.label(
                "Authentication Scheme",
                class_name="block text-sm font-medium mb-2 opacity-80",
            ),
            rx.el.select(
                rx.el.option("Bearer Token"),
                rx.el.option("mTLS"),
                rx.el.option("Basic Auth"),
                default_value=SettingsState.auth_scheme,
                class_name=rx.cond(
                    AppState.is_dark,
                    "w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded-lg focus:ring-2 focus:ring-teal-500/50 outline-none",
                    "w-full px-3 py-2 bg-white border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500/20 outline-none",
                ),
            ),
            class_name="mb-6",
        ),
        rx.el.button(
            "Save Configuration",
            on_click=SettingsState.save_api_config,
            class_name="px-4 py-2 bg-teal-600 hover:bg-teal-700 text-white rounded-lg font-medium transition-colors",
        ),
        class_name="max-w-lg",
    )


def env_row(env: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            env["name"],
            class_name="px-6 py-4 text-sm font-medium text-gray-900 dark:text-white",
        ),
        rx.el.td(
            env["type"],
            class_name="px-6 py-4 text-sm text-gray-500 dark:text-slate-400",
        ),
        rx.el.td(
            env["regions"],
            class_name="px-6 py-4 text-sm text-gray-500 dark:text-slate-400 font-mono",
        ),
        rx.el.td(
            rx.el.button(
                "Edit",
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


def environments_table() -> rx.Component:
    return rx.el.table(
        rx.el.thead(
            rx.el.tr(
                rx.el.th(
                    "Environment",
                    class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                ),
                rx.el.th(
                    "Type",
                    class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                ),
                rx.el.th(
                    "Regions",
                    class_name="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider opacity-70",
                ),
                rx.el.th("", class_name="px-6 py-3"),
            ),
            class_name=rx.cond(
                AppState.is_dark,
                "bg-slate-900 text-slate-300",
                "bg-gray-50 text-gray-500",
            ),
        ),
        rx.el.tbody(rx.foreach(SettingsState.environments, env_row)),
        class_name="w-full",
    )


def plugin_row(plugin: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                plugin["name"], class_name="font-medium text-gray-900 dark:text-white"
            ),
            rx.el.span(
                f"v{plugin['version']}",
                class_name="ml-2 text-xs bg-gray-100 dark:bg-slate-700 px-1.5 py-0.5 rounded text-gray-600 dark:text-slate-300",
            ),
            class_name="flex items-center",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    rx.cond(plugin["enabled"], "Enabled", "Disabled"),
                    class_name="text-sm mr-3 opacity-70",
                ),
                rx.el.button(
                    rx.el.div(
                        class_name=rx.cond(
                            plugin["enabled"],
                            "w-4 h-4 bg-white rounded-full shadow-sm translate-x-5 transition-transform",
                            "w-4 h-4 bg-white rounded-full shadow-sm translate-x-1 transition-transform",
                        )
                    ),
                    on_click=lambda: SettingsState.toggle_plugin(plugin["name"]),
                    class_name=rx.cond(
                        plugin["enabled"],
                        "w-10 h-6 bg-teal-600 rounded-full transition-colors flex items-center",
                        "w-10 h-6 bg-gray-300 dark:bg-slate-600 rounded-full transition-colors flex items-center",
                    ),
                ),
                class_name="flex items-center",
            )
        ),
        class_name=rx.cond(
            AppState.is_dark,
            "flex justify-between items-center p-4 bg-slate-900 rounded-lg border border-slate-700",
            "flex justify-between items-center p-4 bg-gray-50 rounded-lg border border-gray-200",
        ),
    )


def settings_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Settings & Administration",
                class_name=rx.cond(
                    AppState.is_dark,
                    "text-2xl font-bold text-white",
                    "text-2xl font-bold text-gray-900",
                ),
            ),
            class_name="mb-8",
        ),
        settings_section(
            "API Configuration",
            "Manage connection settings for the EMRK control plane API.",
            api_config_form(),
        ),
        settings_section(
            "Environment Definitions",
            "Define the deployment targets available for your engines.",
            environments_table(),
        ),
        settings_section(
            "Plugin Management",
            "Enable or disable engine plugins.",
            rx.el.div(
                rx.foreach(SettingsState.plugins, plugin_row),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
        ),
    )