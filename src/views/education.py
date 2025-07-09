import flet as ft
from components.nav import get_appbar
from data.education_data import university_data, languages_data, courses_data

CARD_RADIUS = 12
UNIVERSITY_HEIGHT = 180
LANGUAGE_HEIGHT = 220
COURSE_ICON_SIZE = 30
PLATFORM_LOGO_SIZE = 40
SECTION_PADDING = 10

def build_university_card(u: dict, city_images: dict) -> ft.Container:
    city_image = city_images.get(u["city"].lower())
    return ft.Container(
        content=ft.Card(
            content=ft.Container(
                content=ft.Stack([
                    ft.Image(
                        src=city_image.src if city_image else "",
                        fit=ft.ImageFit.COVER,
                        expand=True,
                        width=float("inf"),
                        height=float("inf"),
                    ),
                    ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.center_right,
                            end=ft.alignment.center_left,
                            colors=[
                                ft.Colors.with_opacity(0.4, ft.Colors.BLACK),
                                ft.Colors.with_opacity(0.85, ft.Colors.BLACK)
                            ],
                        ),
                        expand=True,
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text(u["title"], size=18, weight="bold", color=ft.Colors.WHITE, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                            ft.Text(u["details"], color=ft.Colors.WHITE70, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                            ft.Text(u["description"], color=ft.Colors.WHITE60, max_lines=3, overflow=ft.TextOverflow.ELLIPSIS),
                        ], spacing=5),
                        padding=20,
                        alignment=ft.alignment.top_left,
                        expand=True,
                    ),
                ]),
                height=UNIVERSITY_HEIGHT,
                width=float("inf"),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                border_radius=CARD_RADIUS,
            ),
            elevation=3,
        ),
        col={"xs": 12, "sm": 12, "md": 6, "xl": 6},
        padding=SECTION_PADDING,
    )

def build_language_card(lang: dict, flags_images: dict) -> ft.Container:
    flag_image = flags_images.get(lang["flag"])
    return ft.Container(
        content=ft.Card(
            content=ft.Stack([
                ft.Image(
                    src=flag_image.src if flag_image else "",
                    width=float("inf"),
                    height=LANGUAGE_HEIGHT,
                    fit=ft.ImageFit.COVER
                ),
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
            height=LANGUAGE_HEIGHT,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
        ),
        col={"xs": 6, "sm": 6, "md": 3},
        padding=5
    )

def build_course_card(course: dict, learning_images: dict) -> ft.Container:
    logo_image = learning_images.get(course["platform"].lower())
    return ft.Container(
        content=ft.Card(
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.SCHOOL, size=COURSE_ICON_SIZE, color=ft.Colors.ORANGE),
                        ft.Container(width=10),
                        ft.Column([
                            ft.Text(course["title"], weight="bold", size=14),
                            ft.Text(course["platform"], size=12, color=ft.Colors.SECONDARY),
                            ft.Text(course["issued"], size=11, color=ft.Colors.SECONDARY),
                        ], alignment=ft.MainAxisAlignment.CENTER, expand=True),
                        ft.Container(
                            content=ft.Image(
                                src=logo_image.src if logo_image else "",
                                fit=ft.ImageFit.CONTAIN,
                                width=PLATFORM_LOGO_SIZE,
                                height=PLATFORM_LOGO_SIZE,
                            ),
                            alignment=ft.alignment.center,
                            width=PLATFORM_LOGO_SIZE,
                            height=PLATFORM_LOGO_SIZE,
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

def build_section_title(title: str) -> ft.Container:
    return ft.Container(
        content=ft.Text(title, size=20, weight="bold"),
        padding=SECTION_PADDING
    )

def view(page: ft.Page, toggle_theme, flags_images, learning_images, city_images):
    university_cards = [build_university_card(u, city_images) for u in university_data]
    language_cards = [build_language_card(lang, flags_images) for lang in languages_data]
    course_cards = [build_course_card(course, learning_images) for course in courses_data]
    page.views.append(
        ft.View(
            route="/education",
            scroll=ft.ScrollMode.AUTO,
            controls=[
                get_appbar("Education", page, on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                build_section_title("University"),
                ft.ResponsiveRow(university_cards, spacing=10, run_spacing=10),
                ft.Divider(),
                build_section_title("Languages"),
                ft.ResponsiveRow(language_cards, spacing=10),
                ft.Divider(),
                build_section_title("Courses & Training"),
                ft.ResponsiveRow(course_cards, spacing=10),
            ]
        )
    )
