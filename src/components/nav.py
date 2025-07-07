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
        title=ft.TextButton(
                  text="Joel Leandro Nardi", 
                  on_click=lambda e: page.go(f"/"), 
                  style=ft.ButtonStyle(
                      text_style=ft.TextStyle(
                          size=18,
                          weight=ft.FontWeight.BOLD,
                          color=ft.Colors.ON_SECONDARY_CONTAINER
                      )
                  )),
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
