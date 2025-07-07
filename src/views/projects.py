import flet as ft
from components.nav import get_appbar

def view(page: ft.Page, toggle_theme):
    projects = [
        {
            "title": "My Portfolio Site",
            "description": "Static portfolio using Flet.",
            "image": "https://via.placeholder.com/300x150",
            "url": "https://github.com/yourname/portfolio"
        },
    ]

    cards = []
    for p in projects:
        card = ft.AnimatedSwitcher(
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Image(src=p["image"], width=300),
                        ft.Text(p["title"], weight="bold"),
                        ft.Text(p["description"]),
                    ]),
                    padding=15,
                    on_click=lambda e, url=p["url"]: page.launch_url(url),
                )
            ),
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=400,
        )
        cards.append(card)

    page.views.append(
        ft.View(
            route="/projects",
            controls=[
                get_appbar("Projects", on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                ft.Wrap(cards, spacing=10, run_spacing=10),
            ]
        )
    )
