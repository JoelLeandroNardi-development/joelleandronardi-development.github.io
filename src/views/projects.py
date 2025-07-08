import flet as ft
from components.nav import get_appbar

def view(page: ft.Page, toggle_theme, tech_images):
    projects = [
        {
            "title": "Small Notes App",
            "description": "Small notes console app as a project to try stuff with node.js",
            "image": tech_images["nodejs"].src if "nodejs" in tech_images else "https://via.placeholder.com/300x150",
            "url": "https://github.com/JoelLeandroNardi-development/notes-app"
        },
        {
            "title": "Rock Paper Scissors Flet App",
            "description": "Simple rock paper scissors game using Flet",
            "image": tech_images["flet"].src if "flet" in tech_images else "https://via.placeholder.com/300x150",
            "url": "https://joelleandronardi-development.github.io/rock-paper-scissors-flet-app/"
        },
        {
            "title": "Power Trade App",
            "description": "Powerfull power trade app written in .NET 9 with a console app and an API",
            "image": tech_images["dotnet"].src if "dotnet" in tech_images else "https://via.placeholder.com/300x150",
            "url": "https://github.com/JoelLeandroNardi-development/PowerTradeApp"
        },
        {
            "title": "Pending Minimal API Example",
            "description": "Under construction minimal API example with .NET 8",
            "image": tech_images["dotnet"].src if "dotnet" in tech_images else "https://via.placeholder.com/300x150",
            "url": "https://github.com/yourname/portfolio"
        },
    ]

    cards = []
    for p in projects:
        card = ft.Card(
            content=ft.Container(
                content=ft.Stack(
                    controls=[
                        ft.Image(
                            src=p["image"],
                            width=float("inf"),
                            height=200,
                            fit=ft.ImageFit.COVER,
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(p["title"], weight="bold", size=16, color=ft.Colors.WHITE),
                                    ft.Text(
                                        p["description"],
                                        size=12,
                                        max_lines=3,
                                        overflow=ft.TextOverflow.ELLIPSIS,
                                        color=ft.Colors.WHITE70,
                                    ),
                                ],
                                spacing=5,
                            ),
                            alignment=ft.alignment.bottom_left,
                            padding=10,
                            bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.BLACK),
                        ),
                    ]
                ),
                height=200,
                border_radius=10,
                on_click=lambda e, url=p["url"]: page.launch_url(url),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
            ),
            elevation=2,
        )
        cards.append(
            ft.Container(
                content=card,
                col={"xs": 12, "sm": 6, "md": 4, "xl": 3},
                padding=5
            )
        )

    page.views.append(
        ft.View(
            route="/projects",
            scroll=ft.ScrollMode.AUTO,
            controls=[
                get_appbar("Projects", page, on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                ft.ResponsiveRow(
                    controls=cards,
                    spacing=10,
                    run_spacing=10,
                )
            ]
        )
    )