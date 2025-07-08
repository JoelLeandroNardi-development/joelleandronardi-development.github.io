import flet as ft
from components.nav import get_appbar

def view(page: ft.Page, toggle_theme=None, avatar=None):

    def on_email_click(e):
        page.launch_url("mailto:joelleandronardi@gmail.com")

    def on_linkedin_click(e):
        page.launch_url("https://linkedin.com/in/joel-leandro-nardi-0b2244a1")

    def on_github_click(e):
        page.launch_url("https://github.com/JoelLeandroNardi-development")

    appbar = get_appbar(
        title="Joel Leandro Nardi",
        page=page,
        toggle_theme=toggle_theme
    )

    name_section = ft.Column(
        controls=[
            ft.Text("Hey there, I am", size=30, weight=ft.FontWeight.W_600),
            ft.Text("Joel Leandro Nardi", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.PRIMARY),
            ft.Row([
                ft.Container(
                    content=ft.Text("Full Stack Developer", size=16, weight=ft.FontWeight.W_500),
                    bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.SECONDARY_CONTAINER),
                    padding=ft.Padding(8, 4, 8, 4),
                    border_radius=8,
                ),
                ft.Container(
                    content=ft.Text("Tech Leader", size=16, weight=ft.FontWeight.W_500),
                    bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.SECONDARY_CONTAINER),
                    padding=ft.Padding(8, 4, 8, 4),
                    border_radius=8,
                ),
                ft.Container(
                    content=ft.Text("Agile Practitioner", size=16, weight=ft.FontWeight.W_500),
                    bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.SECONDARY_CONTAINER),
                    padding=ft.Padding(8, 4, 8, 4),
                    border_radius=8,
                ),
            ]),
            ft.Text(
                "I am an experienced developer building fast, secure, and scalable full-stack web apps.\n"
                "I also have been working as Technical Lead and Agile Delivery Manager.\n"
                "I enjoy solving complex problems and designing user-friendly systems.\n"
                "Information Systems Engineer, graduated from UTN Facultad Regional Rosario (Argentina).\n"
                "Former exchange student and researcher in TU Ilmenau (Germany).\n"
                "Currently living in Spain.",
                size=15,
                opacity=0.8,
            ),
            ft.Row([
                ft.ElevatedButton(
                    content=ft.Row([
                        ft.Icon(name=ft.Icons.EMAIL, color=ft.Colors.WHITE),
                        ft.Text("Email", color=ft.Colors.WHITE),
                    ], spacing=8),
                    bgcolor=ft.Colors.BLUE_400,
                    on_click=on_email_click
                ),
                ft.ElevatedButton(
                    content=ft.Row([
                        ft.Icon(name=ft.Icons.WORK, color=ft.Colors.WHITE),
                        ft.Text("LinkedIn", color=ft.Colors.WHITE),
                    ], spacing=8),
                    bgcolor=ft.Colors.BLUE_300,
                    on_click=on_linkedin_click
                ),
                ft.ElevatedButton(
                    content=ft.Row([
                        ft.Icon(name=ft.Icons.CODE, color=ft.Colors.WHITE),
                        ft.Text("GitHub", color=ft.Colors.WHITE),
                    ], spacing=8),
                    bgcolor=ft.Colors.GREY_900,
                    on_click=on_github_click
                )
            ], spacing=10)
        ],
        spacing=12,
        expand=2
    )

    # --- Responsive Header Layout ---
    header = ft.ResponsiveRow(
        controls=[
            ft.Container(content=name_section, padding=20, col={"xs": 12, "md": 7}),
            ft.Container(
                content=ft.Column(
                    controls=[avatar],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=20,
                col={"xs": 12, "md": 5}
            ),
        ]
    )

    # --- Skill Cards ---
    def skill_card(title, items):
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
            border=ft.border.all(1, ft.Colors.with_opacity(0.2, ft.Colors.PRIMARY)),
            border_radius=12,
            padding=20,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.ON_SURFACE),
            col={"xs": 12, "sm": 6, "md": 4},
        )

    skills_grid = ft.ResponsiveRow([
        skill_card("Languages", ["C#", "Python", "JavaScript", "TypeScript", "YAML"]),
        skill_card("Databases & Cloud", ["SQL Server", "MongoDB", "PostgreSQL", "AWS"]),
        skill_card("Frameworks", [".NET", "React", "Vue", "Flutter"]),
        skill_card("Libraries", ["Redux", "Tailwind", "Axios"]),
        skill_card("CI/CD", ["Docker", "GitHub Actions", "Terraform"]),
        skill_card("UI", ["HTML", "CSS", "Figma"]),
    ], spacing=16, run_spacing=16)

    # --- Final Page Layout ---
    page.views.clear()
    page.views.append(
        ft.View(
            route="/",
            controls=[
                ft.Column(
                    controls=[
                        header,
                        ft.Divider(),
                        ft.Text("Skills", size=28, weight="bold", color=ft.Colors.PRIMARY),
                        ft.Text(
                            "Here are some of my key skills and technologies I've worked with.",
                            size=16,
                            opacity=0.7
                        ),
                        skills_grid,
                    ],
                    spacing=20,
                    expand=True,
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            appbar=appbar,
        )
    )
    page.update()
