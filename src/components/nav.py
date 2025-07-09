import flet as ft

def get_appbar(title: str, page: ft.Page, on_back=None, toggle_theme=None) -> ft.AppBar:
    nav_links = ["education", "projects", "experience", "interests"]
    def navigate(e):
        page.go(f"/{e.control.data.lower()}")
    nav_buttons = [
        ft.TextButton(
            text=link.upper(),
            data=link,
            on_click=navigate,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.ON_SECONDARY_CONTAINER
                )
            )
        ) for link in nav_links
    ]
    popup_menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text=link.title(), data=link, on_click=navigate)
            for link in nav_links
        ]
    )
    def appbar_content():
        is_mobile = page.width <= 600
        leading_controls = []
        if on_back:
            leading_controls.append(ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_back))
        return ft.AppBar(
            leading=ft.Row(
                controls=leading_controls,
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            title=ft.TextButton(
                on_click=lambda e: page.go("/"),
                content=ft.Row(
                    controls=(
                        [
                            ft.Icon(
                                name=ft.Icons.DATA_ARRAY_ROUNDED,
                                size=36,
                                color=ft.Colors.ON_TERTIARY_CONTAINER
                            )
                        ]
                        if is_mobile else
                        [
                            ft.Icon(
                                name=ft.Icons.DATA_ARRAY_ROUNDED,
                                size=36,
                                color=ft.Colors.ON_TERTIARY_CONTAINER
                            ),
                            ft.Text(
                                "Joel Leandro Nardi",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.ON_TERTIARY_CONTAINER,
                            )
                        ]
                    ),
                    spacing=8,
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                ),
                style=ft.ButtonStyle(
                    padding=0,
                    shape=ft.RoundedRectangleBorder(radius=0),
                    bgcolor="transparent",
                    overlay_color="transparent",
                    elevation={"hovered": 0, "pressed": 0}
                )
            ),
            center_title=False,
            bgcolor=ft.Colors.SECONDARY_CONTAINER,
            actions=[
                popup_menu if is_mobile else ft.Row(controls=nav_buttons, spacing=12),
                ft.IconButton(
                    icon=ft.Icons.DARK_MODE,
                    tooltip="Toggle Dark Mode",
                    on_click=toggle_theme,
                ),
            ]
        )
    def resize_handler(e):
        page.appbar = appbar_content()
        page.update()
    page.on_resize = resize_handler
    return appbar_content()
