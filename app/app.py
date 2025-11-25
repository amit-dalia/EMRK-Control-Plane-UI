import reflex as rx
from app.states.app_state import AppState
from app.components.layout import layout
from app.components.dashboard_views import global_dashboard
from app.components.engine_views import engines_page, engine_detail_page
from app.components.cluster_views import cluster_detail_page
from app.components.jobs_views import jobs_page
from app.components.telemetry_views import telemetry_page
from app.components.logs_views import logs_page
from app.components.settings_views import settings_page


def index() -> rx.Component:
    return layout(global_dashboard())


def engines() -> rx.Component:
    return layout(engines_page())


def engine_detail() -> rx.Component:
    return layout(engine_detail_page())


def cluster_detail() -> rx.Component:
    return layout(cluster_detail_page())


def jobs() -> rx.Component:
    return layout(jobs_page())


def telemetry() -> rx.Component:
    return layout(telemetry_page())


def logs() -> rx.Component:
    return layout(logs_page())


def settings() -> rx.Component:
    return layout(settings_page())


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(engines, route="/engines")
app.add_page(engine_detail, route="/engines/[engine_id]")
app.add_page(cluster_detail, route="/clusters/[cluster_id]")
app.add_page(jobs, route="/jobs")
app.add_page(telemetry, route="/telemetry")
app.add_page(logs, route="/logs")
app.add_page(settings, route="/settings")