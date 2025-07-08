import flet as ft
from components.nav import get_appbar

def view(page: ft.Page, toggle_theme, flags_images):
    # ---------- UNIVERSITY SECTION ----------
    university_cards = [
        ft.Container(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Information Systems Engineering Degree", size=18, weight="bold"),
                        ft.Text("🇦🇷 Universidad Tecnológica Nacional | 2014 - 2019"),
                        ft.Text("Focused on software development, AI, and data systems."),
                    ], spacing=5),
                    padding=20,
                ),
                elevation=3
            ),
            col={"xs": 12, "sm": 12, "md": 6, "xl": 6},  # ✅ half width on md+ screens
            padding=10
        ),
        ft.Container(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Research in Computer & Systems Engineering (M. Sc.)", size=18, weight="bold"),
                        ft.Text("🇩🇪 Technische Universität Ilmenau | 2018 - 2019 (Exchange Program)"),
                        ft.Text("Specializing in ML, NLP, and advanced algorithms."),
                    ], spacing=5),
                    padding=20,
                ),
                elevation=3
            ),
            col={"xs": 12, "sm": 12, "md": 6, "xl": 6},  # ✅ half width on md+ screens
            padding=10
        ),
    ]

    # ---------- LANGUAGES SECTION ----------
    languages = [
        {"name": "English", "level": "Bilingual", "flag": "uk"},
        {"name": "Spanish", "level": "Native", "flag": "spain"},
        {"name": "Italian", "level": "Intermediate", "flag": "italy"},
        {"name": "German", "level": "Intermediate", "flag": "germany"},
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
        for lang in languages
    ]

    # ---------- COURSES / TRAINING ----------
    courses = [
        {"title": "Complete Python Bootcamp", "platform": "Udemy", "url": "https://www.udemy.com/course/complete-python-bootcamp/"},
        {"title": "Advanced React", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/react-advanced"},
        {"title": "Machine Learning A-Z", "platform": "Udemy", "url": "https://www.udemy.com/course/machinelearning/"},
        {"title": "Clean Architecture in .NET", "platform": "Pluralsight", "url": "https://www.pluralsight.com/courses/clean-architecture-dotnet"},
    ]

    course_cards = [
        ft.Container(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(course["title"], weight="bold", size=14),
                        ft.Text(course["platform"], size=12, color=ft.Colors.SECONDARY),
                    ]),
                    padding=10,
                    on_click=lambda e, url=course["url"]: page.launch_url(url),
                ),
                elevation=1
            ),
            col={"xs": 12, "sm": 6, "md": 4, "xl": 3},
            padding=5
        )
        for course in courses
    ]

    # ---------- APPEND TO PAGE ----------
    page.views.append(
        ft.View(
            route="/education",
            scroll=ft.ScrollMode.AUTO,
            controls=[
                get_appbar("Education", page, on_back=lambda e: page.go("/"), toggle_theme=toggle_theme),
                ft.Container(
                    content=ft.Text("University", size=20, weight="bold"),
                    padding=10
                ),
                ft.ResponsiveRow(university_cards, spacing=10, run_spacing=10),
                ft.Divider(),
                ft.Container(
                    content=ft.Text("Languages", size=20, weight="bold"),
                    padding=10
                ),
                ft.ResponsiveRow(language_cards, spacing=10),
                ft.Divider(),
                ft.Container(
                    content=ft.Text("Courses & Training", size=20, weight="bold"),
                    padding=10
                ),
                ft.ResponsiveRow(course_cards, spacing=10),
            ]
        )
    )