import flet as ft
from components.nav import get_appbar

def view(page: ft.Page, toggle_theme):
    education = ft.Column([
        ft.Text("B.Sc. in Computer Science - XYZ University (2015-2019)", size=16),
        ft.Text("Relevant Coursework: Data Structures, Algorithms, AI, Web Development")
    ], spacing=10)

    page.views.append(
        ft.View(
            route="/education",
            controls=[
                get_appbar("Education", on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                education,
            ]
        )
    )
