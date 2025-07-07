import flet as ft
from components.nav import get_appbar

def view(page: ft.Page, toggle_theme):
    contacts = ft.Column([
        ft.ListTile(title=ft.Text("Email: your.email@example.com")),
        ft.ListTile(title=ft.Text("LinkedIn: linkedin.com/in/yourprofile")),
        ft.ListTile(title=ft.Text("GitHub: github.com/yourusername"))
    ], spacing=10)

    page.views.append(
        ft.View(
            route="/contact",
            controls=[
                get_appbar("Contact", on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                contacts
            ]
        )
    )
