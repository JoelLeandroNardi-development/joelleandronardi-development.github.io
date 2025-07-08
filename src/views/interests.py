# views/interests.py
import flet as ft
from components.nav import get_appbar

def view(page: ft.Page, toggle_theme):
    interests = ft.Text(
        "I enjoy solving problems through technology, hiking, photography, and learning new languages."
    )

    page.views.append(
        ft.View(
            route="/interests",
            scroll=ft.ScrollMode.AUTO,
            controls=[
                get_appbar("Interests", page, on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                interests
            ]
        )
    )
