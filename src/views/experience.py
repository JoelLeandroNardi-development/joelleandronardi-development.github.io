import flet as ft
from components.nav import get_appbar
from data.experience_data import experiences

CARD_RADIUS = 12
OPACITY_LIGHT_BG = 0.02
OPACITY_INNER_BG = 0.03
OPACITY_ROLE_BG = 0.08
LOGO_SIZE = 50
ICON_SIZE = 20
TIMELINE_LINE_HEIGHT = 80

def create_timeline_icon(is_last: bool) -> ft.Column:
    return ft.Column(
        [
            ft.Container(
                content=ft.Icon(name=ft.Icons.WORK, size=ICON_SIZE, color=ft.Colors.WHITE),
                width=40,
                height=40,
                bgcolor=ft.Colors.BLUE,
                border_radius=20,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                width=2,
                height=TIMELINE_LINE_HEIGHT,
                bgcolor=ft.Colors.BLUE_200 if not is_last else ft.Colors.TRANSPARENT,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

def create_role_details(role: dict) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(role["title"], weight="bold", size=16),
                ft.Text(f'{role["start_date"]} – {role["end_date"]}', size=12, italic=True),
                ft.Text(role["description"], size=13),
                ft.Text("Skills: " + ", ".join(role["skills"]), size=11, italic=True),
            ],
            spacing=8,
        ),
        padding=15,
        bgcolor=ft.Colors.with_opacity(OPACITY_ROLE_BG, ft.Colors.ON_SECONDARY_CONTAINER),
        border_radius=CARD_RADIUS,
        expand=True,
    )

def create_timeline_role(role: dict, is_last=False) -> ft.Row:
    return ft.Row(
        [
            create_timeline_icon(is_last),
            create_role_details(role),
        ],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
        spacing=15,
    )

def create_company_logo(company_key: str, companies_images: dict) -> ft.Container:
    logo_img = companies_images.get(company_key.lower())
    logo = (
        ft.Image(src=logo_img.src, width=LOGO_SIZE, height=LOGO_SIZE)
        if logo_img else ft.Container(width=LOGO_SIZE, height=LOGO_SIZE)
    )
    return ft.Container(
        content=logo,
        alignment=ft.alignment.center,
        width=LOGO_SIZE,
        height=LOGO_SIZE,
        border_radius=LOGO_SIZE / 2,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

def create_company_title(company_data: dict, companies_images: dict) -> ft.Row:
    return ft.Row(
        [
            create_company_logo(company_data["key"], companies_images),
            ft.Text(company_data["company"], size=18, weight="bold"),
        ],
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

def create_company_card(company_data: dict, companies_images: dict) -> ft.Container:
    roles = company_data["roles"]
    role_widgets = [
        create_timeline_role(role, is_last=(i == len(roles) - 1))
        for i, role in enumerate(roles)
    ]

    return ft.Container(
        content=ft.ExpansionTile(
            title=create_company_title(company_data, companies_images),
            subtitle=ft.Text(company_data["location_type"], size=12, italic=True),
            controls=[
                ft.Container(
                    content=ft.Column(role_widgets, spacing=20),
                    padding=10,
                    bgcolor=ft.Colors.with_opacity(OPACITY_INNER_BG, ft.Colors.ON_SECONDARY_CONTAINER),
                    border_radius=CARD_RADIUS,
                )
            ],
        ),
        padding=15,
        border_radius=CARD_RADIUS,
        bgcolor=ft.Colors.with_opacity(OPACITY_LIGHT_BG, ft.Colors.ON_SECONDARY_CONTAINER),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

def view(page: ft.Page, toggle_theme, companies_images: dict):
    company_cards = [create_company_card(company, companies_images) for company in experiences]
    page.views.append(
        ft.View(
            route="/experience",
            scroll=ft.ScrollMode.AUTO,
            controls=[
                get_appbar("Experience", page, on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                ft.Container(
                    alignment=ft.alignment.top_center,
                    padding=20,
                    content=ft.ResponsiveRow(
                        columns=12,
                        controls=[
                            ft.Container(
                                content=ft.Column(company_cards, spacing=20),
                                col={"sm": 12, "md": 12, "lg": 12, "xl": 12},
                                padding=20,
                                bgcolor=ft.Colors.with_opacity(OPACITY_LIGHT_BG, ft.Colors.ON_SECONDARY_CONTAINER),
                                border_radius=CARD_RADIUS,
                            )
                        ]
                    ),
                    width=page.width,
                ),
            ],
        )
    )
