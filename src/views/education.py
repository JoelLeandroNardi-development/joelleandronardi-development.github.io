import flet as ft
from components.nav import get_appbar
from data.education_data import university_data, languages_data, courses_data

def view(page: ft.Page, toggle_theme, flags_images, learning_images):
    university_cards = [
        ft.Container(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(u["title"], size=18, weight="bold"),
                        ft.Text(u["details"]),
                        ft.Text(u["description"]),
                    ], spacing=5),
                    padding=20,
                ),
                elevation=3
            ),
            col={"xs": 12, "sm": 12, "md": 6, "xl": 6},
            padding=10
        )
        for u in university_data
    ]

    language_cards = [
        ft.Container(
            content=ft.Card(
                content=ft.Stack([
                    ft.Image(src=flags_images[lang["flag"]].src, width=float("inf"), height=220, fit=ft.ImageFit.COVER),
                    ft.Container(
                        content=ft.Column([
                            ft.Text(lang["name"], color=ft.Colors.WHITE, weight="bold", size=16),
                            ft.Text(lang["level"], color=ft.Colors.WHITE70, size=12),
                        ]),
                        alignment=ft.alignment.bottom_left,
                        padding=10,
                        bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.BLACK),
                        expand=True,
                    )
                ]),
                height=220,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
            ),
            col={"xs": 6, "sm": 6, "md": 3},
            padding=5
        )
        for lang in languages_data
    ]

    course_cards = [
        ft.Container(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.SCHOOL, size=30, color=ft.Colors.ORANGE),
                            ft.Container(width=10),
                            ft.Column([
                                ft.Text(course["title"], weight="bold", size=14),
                                ft.Text(course["platform"], size=12, color=ft.Colors.SECONDARY),
                                ft.Text(course["issued"], size=11, color=ft.Colors.SECONDARY),
                            ], alignment=ft.MainAxisAlignment.CENTER, expand=True),
                            ft.Container(
                                content=ft.Image(
                                    src=learning_images[course["platform"].lower()].src,
                                    fit=ft.ImageFit.CONTAIN,
                                    width=40,
                                    height=40,
                                ),
                                alignment=ft.alignment.center,
                                width=40,
                                height=40,
                                border_radius=20,
                                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                    ),
                    padding=10,
                    expand=True,
                ),
                elevation=1
            ),
            col={"xs": 12, "sm": 6, "md": 4, "xl": 3},
            padding=5,
            expand=True,
        )
        for course in courses_data
    ]

    page.views.append(
        ft.View(
            route="/education",
            scroll=ft.ScrollMode.AUTO,
            controls=[
                get_appbar("Education", page, on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                ft.Container(content=ft.Text("University", size=20, weight="bold"), padding=10),
                ft.ResponsiveRow(university_cards, spacing=10, run_spacing=10),
                ft.Divider(),
                ft.Container(content=ft.Text("Languages", size=20, weight="bold"), padding=10),
                ft.ResponsiveRow(language_cards, spacing=10),
                ft.Divider(),
                ft.Container(content=ft.Text("Courses & Training", size=20, weight="bold"), padding=10),
                ft.ResponsiveRow(course_cards, spacing=10),
            ]
        )
    )
