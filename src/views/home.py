import flet as ft

def view(page: ft.Page, toggle_theme=None):

    # Your existing click handlers (add more if you want for nav links)
    def on_email_click(e):
        page.launch_url("mailto:joelleandronardi@gmail.com")

    def on_linkedin_click(e):
        page.launch_url("https://linkedin.com/in/joel-leandro-nardi-0b2244a1")

    def on_github_click(e):
        page.launch_url("https://github.com/JoelLeandroNardi-development")

    # Navigation click handlers
    def on_nav_click(e):
        # You can expand this to navigate or scroll to sections, or open URLs
        print(f"Clicked {e.control.data}")

    # Header navigation bar
    nav_links = ["Courses", "Education", "Projects", "Experience", "Interests"]

    header_nav = ft.Container(
        content=ft.Row(
            controls=[
                ft.TextButton(
                    text=link,
                    data=link,
                    on_click=on_nav_click,
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(color=ft.Colors.AMBER)
                    )
                )
                for link in nav_links
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=24
        ),
        padding=ft.Padding(10, 10, 10, 10),
        bgcolor=ft.Colors.GREY_900,
    )

    avatar = ft.Image(
        src="assets/avatar.png",
        width=180,
        height=180,
        border_radius=90,
    )

    name_section = ft.Column(
        controls=[
            ft.Text("Hi, I am", size=30, weight=ft.FontWeight.W_600),
            ft.Text("Joel Leandro Nardi", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.AMBER),
            ft.Container(
                content=ft.Text("Full Stack Developer", size=16, weight=ft.FontWeight.W_500),
                bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.AMBER_100),
                padding=ft.Padding(8, 4, 8, 4),
                border_radius=8,
            ),
            ft.Text(
                "I’m an experienced developer building fast, secure, and scalable full-stack web apps.\n"
                "I enjoy solving complex problems and designing user-friendly systems.",
                size=15,
                opacity=0.8,
            ),
            ft.Row([
                ft.ElevatedButton("Quick Mail", on_click=on_email_click, bgcolor=ft.Colors.BLUE_400),
                ft.ElevatedButton("LinkedIn", on_click=on_linkedin_click, bgcolor=ft.Colors.BLUE_300),
                ft.ElevatedButton("GitHub", on_click=on_github_click, bgcolor=ft.Colors.GREY_900),
            ], spacing=10),
        ],
        spacing=12,
        expand=2
    )

    header = ft.ResponsiveRow(
        controls=[
            ft.Container(content=name_section, padding=20, col={"xs": 12, "md": 7}),
            ft.Container(content=avatar, alignment=ft.alignment.center, padding=20, col={"xs": 12, "md": 5}),
        ]
    )

    def skill_card(title, items):
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=16, weight="bold", color=ft.Colors.AMBER_200),
                ft.Row(
                    controls=[ft.Chip(label=ft.Text(skill)) for skill in items],
                    wrap=True,
                    spacing=8,
                    run_spacing=8,
                ),
            ]),
            border=ft.border.all(1, ft.Colors.with_opacity(0.2, ft.Colors.AMBER_100)),
            border_radius=12,
            padding=20,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.ON_SURFACE),
            col={"xs": 12, "sm": 6, "md": 4},
        )

    skills_grid = ft.ResponsiveRow([
        skill_card("Languages", ["Python", "JavaScript", "Go", "Java"]),
        skill_card("Databases & Cloud", ["PostgreSQL", "MongoDB", "Firebase", "AWS"]),
        skill_card("Frameworks", ["React", "Next.js", "Express", "Flutter"]),
        skill_card("Libraries", ["Redux", "Tailwind", "Axios"]),
        skill_card("CI/CD", ["Docker", "GitHub Actions", "Vercel"]),
        skill_card("UI", ["HTML", "CSS", "Figma"]),
    ], spacing=16, run_spacing=16)

    page.views.clear()
    page.views.append(
        ft.View(
            "/",
            controls=[
                ft.Column(
                    [
                        header_nav,   # <--- add header nav here
                        header,
                        ft.Divider(),
                        ft.Text("Skills", size=28, weight="bold", color=ft.Colors.AMBER),
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
        )
    )
    page.update()
