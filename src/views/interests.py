import flet as ft
from components.nav import get_appbar
from data.interests_data import interests

def build_interest_card(interest: dict, interest_images: dict) -> ft.Container:
    image = interest_images.get(interest["key"])
    return ft.Container(
        col={"xs": 12, "sm": 6, "md": 4},
        padding=10,
        content=ft.Card(
            elevation=2,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Column(
                controls=[
                    ft.Image(
                        src=image.src if image else None,
                        width=float("inf"),
                        height=160,
                        fit=ft.ImageFit.COVER,
                        error_content=ft.Text("Image not available", size=12, italic=True, color=ft.Colors.ERROR),
                    ),
                    ft.Container(
                        padding=10,
                        content=ft.Column([
                            ft.Text(interest["title"], size=16, weight="bold"),
                            ft.Text(interest["description"], size=12, color=ft.Colors.SECONDARY),
                        ])
                    )
                ]
            )
        )
    )

def view(page: ft.Page, toggle_theme, interest_images: dict):
    interest_cards = [build_interest_card(i, interest_images) for i in interests]
    page.views.append(
        ft.View(
            route="/interests",
            scroll=ft.ScrollMode.AUTO,
            controls=[
                get_appbar("Interests", page, on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                ft.Container(
                    padding=10,
                    content=ft.ResponsiveRow(interest_cards, spacing=10, run_spacing=10),
                )
            ]
        )
    )
