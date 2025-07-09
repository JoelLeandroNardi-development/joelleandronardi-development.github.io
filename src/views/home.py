import flet as ft
from components.nav import get_appbar

SECTION_PADDING = 20
PRIMARY_OPACITY = 0.05
BORDER_OPACITY = 0.2
TEXT_OPACITY = 0.8

def on_email_click(e, page): page.launch_url("mailto:joelleandronardi@gmail.com")
def on_linkedin_click(e, page): page.launch_url("https://linkedin.com/in/joel-leandro-nardi-0b2244a1")
def on_github_click(e, page): page.launch_url("https://github.com/JoelLeandroNardi-development")

def build_title_row(texts: list[str]) -> ft.Row:
    return ft.Row([
        ft.Container(
            content=ft.Text(label, size=16, weight=ft.FontWeight.W_500),
            bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.SECONDARY_CONTAINER),
            padding=ft.Padding(8, 4, 8, 4),
            border_radius=8,
        ) for label in texts
    ])

def build_contact_buttons(page: ft.Page) -> ft.Row:
    return ft.Row([
        ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(name=ft.Icons.EMAIL, color=ft.Colors.WHITE),
                ft.Text("Email", color=ft.Colors.WHITE),
            ], spacing=8),
            bgcolor=ft.Colors.BLUE_400,
            on_click=lambda e: on_email_click(e, page)
        ),
        ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(name=ft.Icons.WORK, color=ft.Colors.WHITE),
                ft.Text("LinkedIn", color=ft.Colors.WHITE),
            ], spacing=8),
            bgcolor=ft.Colors.BLUE_300,
            on_click=lambda e: on_linkedin_click(e, page)
        ),
        ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(name=ft.Icons.CODE, color=ft.Colors.WHITE),
                ft.Text("GitHub", color=ft.Colors.WHITE),
            ], spacing=8),
            bgcolor=ft.Colors.GREY_900,
            on_click=lambda e: on_github_click(e, page)
        )
    ], spacing=10)

def build_name_section(page: ft.Page) -> ft.Column:
    return ft.Column(
        controls=[
            ft.Text("Hey there, I am", size=30, weight=ft.FontWeight.W_600),
            ft.Text("Joel Leandro Nardi", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.PRIMARY),
            build_title_row(["Full Stack Developer", "Tech Leader", "Agile Practitioner"]),
            ft.Text(
                "Experienced developer building fast, secure, and scalable full-stack web apps.\n"
                "Years of Technical Lead and Agile Delivery Manager expertise.\n"
                "Information Systems Engineer, graduated from UTN Facultad Regional Rosario (Argentina).\n"
                "Former exchange student and researcher in TU Ilmenau (Germany).\n"
                "Currently residing in Spain.",
                size=15,
                opacity=TEXT_OPACITY,
            ),
            build_contact_buttons(page)
        ],
        spacing=12,
        expand=2
    )

def build_avatar_column(avatar) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            controls=[avatar],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=SECTION_PADDING,
        col={"xs": 12, "md": 5}
    )

def build_header_section(page: ft.Page, avatar) -> ft.ResponsiveRow:
    return ft.ResponsiveRow(
        controls=[
            ft.Container(content=build_name_section(page), padding=SECTION_PADDING, col={"xs": 12, "md": 7}),
            build_avatar_column(avatar),
        ]
    )

def skill_card(title: str, items: list[str]) -> ft.Container:
    return ft.Container(
        content=ft.Column([
            ft.Text(title, size=16, weight="bold", color=ft.Colors.PRIMARY),
            ft.Row(
                controls=[ft.Chip(label=ft.Text(skill)) for skill in items],
                wrap=True,
                spacing=8,
                run_spacing=8,
            ),
        ]),
        border=ft.border.all(1, ft.Colors.with_opacity(BORDER_OPACITY, ft.Colors.PRIMARY)),
        border_radius=12,
        padding=20,
        bgcolor=ft.Colors.with_opacity(PRIMARY_OPACITY, ft.Colors.ON_SURFACE),
        col={"xs": 12, "sm": 6, "md": 4},
    )

def build_skills_grid() -> ft.ResponsiveRow:
    return ft.ResponsiveRow([
        skill_card("Languages", ["C#", "Python", "JavaScript", "TypeScript", "YAML"]),
        skill_card("Databases & Cloud", ["SQL Server", "MongoDB", "PostgreSQL", "AWS"]),
        skill_card("Frameworks", [".NET", "React", "Vue", "Flutter"]),
        skill_card("Libraries", ["Redux", "Entity Framework", "Axios", "Ngrx"]),
        skill_card("CI/CD", ["Docker", "GitHub Actions", "Terraform"]),
        skill_card("UI", ["HTML", "CSS", "Figma"]),
    ], spacing=16, run_spacing=16)

def view(page: ft.Page, toggle_theme=None, avatar=None):
    page.views.clear()

    page.views.append(
        ft.View(
            route="/",
            controls=[
                ft.Column(
                    controls=[
                        build_header_section(page, avatar),
                        ft.Divider(),
                        ft.Text("Skills", size=28, weight="bold", color=ft.Colors.PRIMARY),
                        ft.Text(
                            "Here are some of my key skills and technologies I've worked with.",
                            size=16,
                            opacity=0.7
                        ),
                        build_skills_grid(),
                    ],
                    spacing=20,
                    expand=True,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            appbar=get_appbar("Joel Leandro Nardi", page=page, toggle_theme=toggle_theme),
        )
    )
    page.update()
