import flet as ft

def get_appbar(title: str, on_back=None, toggle_theme=None) -> ft.AppBar:
    return ft.AppBar(
        leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=on_back) if on_back else None,
        title=ft.Text(title),
        center_title=True,
        actions=[
            ft.IconButton(
                icon=ft.Icons.DARK_MODE,
                tooltip="Toggle Dark Mode",
                on_click=toggle_theme,
            )
        ]
    )
