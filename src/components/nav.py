import flet as ft

def get_appbar(title: str, page: ft.Page, on_back=None, toggle_theme=None) -> ft.AppBar:
    nav_links = ["education", "projects", "experience", "interests"]

    # Only add back button if on_back is provided
    leading_controls = []
    if on_back:
        leading_controls.append(
            ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_back)
        )

    return ft.AppBar(
        leading=ft.Row(
            controls=leading_controls,
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        title=ft.Row(  # Wrap the title button in a Row to make it expand
            controls=[
                ft.TextButton(
                    on_click=lambda e: page.go("/"),
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                name=ft.Icons.DATA_ARRAY_ROUNDED,
                                size=36,
                                color=ft.Colors.ON_TERTIARY_CONTAINER
                            ),
                            ft.Text(
                                "Joel Leandro Nardi ",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.ON_TERTIARY_CONTAINER,
                            ),
                        ],
                        spacing=8,
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True  # Make text+icon row expand
                    ),
                    style=ft.ButtonStyle(
                        padding=0,
                        shape=ft.RoundedRectangleBorder(radius=0),
                    )
                )
            ],
            expand=True,  # Make title row fill horizontal space
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        center_title=False,
        bgcolor=ft.Colors.SECONDARY_CONTAINER,
        actions=[
            ft.Row(
                controls=[
                    ft.TextButton(
                        text=link.upper(),
                        data=link,
                        on_click=lambda e: page.go(f"/{e.control.data.lower()}"),
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.ON_SECONDARY_CONTAINER
                            )
                        )
                    )
                    for link in nav_links
                ],
                spacing=16,
            ),
            ft.IconButton(
                icon=ft.Icons.DARK_MODE,
                tooltip="Toggle Dark Mode",
                on_click=toggle_theme,
            ),
        ]
    )
