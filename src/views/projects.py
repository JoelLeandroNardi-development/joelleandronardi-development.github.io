import flet as ft
from components.nav import get_appbar
from data.projects_data import projects

def build_project_card(project: dict, page: ft.Page, tech_images: dict) -> ft.Container:
    image_url = tech_images.get(project["tech"], None)
    image_src = image_url.src if image_url else "https://via.placeholder.com/300x150"

    return ft.Container(
        content=ft.Card(
            content=ft.Container(
                content=ft.Stack(
                    controls=[
                        ft.Image(
                            src=image_src,
                            width=float("inf"),
                            height=200,
                            fit=ft.ImageFit.COVER,
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(project["title"], weight="bold", size=16, color=ft.Colors.WHITE),
                                    ft.Text(
                                        project["description"],
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
                on_click=lambda e: page.launch_url(project["url"]),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
            ),
            elevation=2,
        ),
        col={"xs": 12, "sm": 6, "md": 4, "xl": 3},
        padding=5
    )

def view(page: ft.Page, toggle_theme, tech_images):
    page.views.append(
        ft.View(
            route="/projects",
            scroll=ft.ScrollMode.AUTO,
            controls=[
                get_appbar("Projects", page, on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                ft.ResponsiveRow(
                    controls=[
                        build_project_card(p, page, tech_images) for p in projects
                    ],
                    spacing=10,
                    run_spacing=10,
                )
            ]
        )
    )
