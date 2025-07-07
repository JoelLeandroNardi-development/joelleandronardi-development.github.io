import flet as ft
from components.nav import get_appbar

def view(page: ft.Page, toggle_theme):
    courses = [
        "Machine Learning - Coursera",
        "Responsive Web Design - freeCodeCamp",
        "Cloud Fundamentals - Microsoft Learn"
    ]

    list_items = [ft.ListTile(title=ft.Text(c)) for c in courses]

    page.views.append(
        ft.View(
            route="/courses",
            controls=[
                get_appbar("Courses & Certifications", on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                ft.Column(list_items, scroll=ft.ScrollMode.AUTO),
            ]
        )
    )
