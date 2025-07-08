import flet as ft
from datetime import datetime
from dateutil.relativedelta import relativedelta
from components.nav import get_appbar
from data.experience_data import experiences

def format_duration(start_str, end_str):
    start = datetime.strptime(start_str, "%b %Y")
    end = datetime.now() if end_str.lower() in ["present", "now"] else datetime.strptime(end_str, "%b %Y")
    delta = relativedelta(end, start)
    years = f"{delta.years} yr{'s' if delta.years != 1 else ''}" if delta.years else ""
    months = f"{delta.months} mo{'s' if delta.months != 1 else ''}" if delta.months else ""
    return " · ".join(filter(None, [years, months]))

def create_timeline_role(role, is_last=False):
    duration = format_duration(role["start_date"], role["end_date"])

    return ft.Row(
        [
            ft.Column(
                [
                    ft.Container(
                        content=ft.Icon(name=ft.Icons.WORK, size=20, color=ft.Colors.WHITE),
                        width=40,
                        height=40,
                        bgcolor=ft.Colors.BLUE,
                        border_radius=20,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        width=2,
                        padding=0,
                        height=80,
                        bgcolor=ft.Colors.BLUE_200 if not is_last else ft.Colors.TRANSPARENT,
                        margin=ft.margin.only(top=0),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(role["title"], weight="bold", size=16),
                        ft.Text(f'{role["start_date"]} – {role["end_date"]} · {duration}', size=12, italic=True),
                        ft.Text(role["description"], size=13),
                        ft.Text("Skills: " + ", ".join(role["skills"]), size=11, italic=True),
                    ],
                    spacing=8,
                ),
                padding=15,
                bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.ON_SECONDARY_CONTAINER),
                border_radius=12,
                expand=True,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
        spacing=15,
    )

def create_company_card(company_data):
    roles = company_data["roles"]
    role_widgets = [
        create_timeline_role(role, is_last=(i == len(roles) - 1))
        for i, role in enumerate(roles)
    ]

    return ft.Container(
        content=ft.ExpansionTile(
            title=ft.Text(company_data["company"], size=18, weight="bold"),
            subtitle=ft.Text(company_data["location_type"], size=12, italic=True),
            controls=[
                ft.Container(
                    content=ft.Column(role_widgets, spacing=20),
                    padding=10,
                    bgcolor=ft.Colors.with_opacity(0.03, ft.Colors.ON_SECONDARY_CONTAINER),
                    border_radius=8,
                )
            ],
        ),
        padding=15,
        border_radius=12,
        bgcolor=ft.Colors.with_opacity(0.02, ft.Colors.ON_SECONDARY_CONTAINER),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )

def view(page: ft.Page, toggle_theme):
    company_cards = [create_company_card(company) for company in experiences]

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
                                bgcolor=ft.Colors.with_opacity(0.02, ft.Colors.ON_SECONDARY_CONTAINER),
                                border_radius=12,
                            )
                        ]
                    ),
                    width=page.width,
                ),
            ],
        )
    )
