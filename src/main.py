import flet as ft
from views import home, projects, experience, education, interests

def main(page: ft.Page):
    avatar = ft.Image(
            src="avatar.png",
            width=180,
            height=180,
            border_radius=90,
        )
    tech_images = {
        "dotnet": ft.Image(src="dotnet.png"),
        "nodejs": ft.Image(src="nodejs.png"),
        "flet": ft.Image(src="flet.png"),
    }
    flags_images = {
        "uk": ft.Image(src="flags/uk_flag.png"),
        "spain": ft.Image(src="flags/sp_flag.png"),
        "italy": ft.Image(src="flags/it_flag.png"),
        "germany": ft.Image(src="flags/de_flag.png"),
    }
    learning_images = {
        "pluralsight": ft.Image(src="learning/pluralsight.png"),
        "udemy": ft.Image(src="learning/udemy.png"),
    }
    city_images = {
        "rosario": ft.Image(src="cities/rosario.jpg"),
        "ilmenau": ft.Image(src="cities/ilmenau.jpg"),
    }
    companies_images = {
        "softtek": ft.Image(src="experience/softtek.png"),
        "acsys": ft.Image(src="experience/acsys.png"),
        "sweatworks": ft.Image(src="experience/sweatworks.png"),
        "tiarg": ft.Image(src="experience/tiarg.png"),
        "globant": ft.Image(src="experience/globant.png"),
        "tecso": ft.Image(src="experience/tecso.png"),
        "utn": ft.Image(src="experience/utn.png"),
    }

    is_dark = True
    def toggle_theme(e=None):
        nonlocal is_dark
        is_dark = not is_dark
        page.theme_mode = ft.ThemeMode.DARK if is_dark else ft.ThemeMode.LIGHT
        page.update()

    def route_change(e):
        page.views.clear()
        route = page.route

        if route == "/":
            home.view(page, toggle_theme, avatar)
        elif route == "/projects":
            projects.view(page, toggle_theme, tech_images)
        elif route == "/experience":
            experience.view(page, toggle_theme, companies_images)
        elif route == "/education":
            education.view(page, toggle_theme, flags_images, learning_images, city_images)
        elif route == "/interests":
            interests.view(page, toggle_theme)
        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")