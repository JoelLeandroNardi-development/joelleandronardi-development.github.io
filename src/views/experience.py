import flet as ft
from components.nav import get_appbar

def view(page: ft.Page, toggle_theme):
    experiences = [
        {"company": "Pending", "role": "Software Engineer", "duration": "2021 - Present", "promotions": ["Junior Dev", "Mid-Level Dev", "Senior Dev"]},
        {"company": "Pending", "role": "Frontend Developer", "duration": "2019 - 2021", "promotions": []}
    ]

    cards = []
    for exp in experiences:
        promotion_text = ft.Text(", ".join(exp["promotions"])) if exp["promotions"] else ft.Text("No promotions listed")
        card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text(exp["company"], size=20, weight="bold"),
                    ft.Text(f"Role: {exp['role']}", italic=True),
                    ft.Text(f"Duration: {exp['duration']}", size=12),
                    promotion_text
                ]),
                padding=15,
            )
        )
        cards.append(card)

    page.views.append(
        ft.View(
            route="/experience",
            scroll=ft.ScrollMode.AUTO,
            controls=[
                get_appbar("Experience", page, on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                ft.Column(cards, scroll=ft.ScrollMode.ADAPTIVE),
            ]
        )
    )
    