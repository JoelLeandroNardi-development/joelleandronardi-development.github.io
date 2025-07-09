import flet as ft
from views import home, projects, experience, education, interests

NAV_ROUTES = {
    "/": home.view,
    "/projects": projects.view,
    "/experience": experience.view,
    "/education": education.view,
    "/interests": interests.view,
}

def load_images(image_map: dict[str, list[str]], base_path: str) -> dict[str, ft.Image]:
    return {
        key: ft.Image(src=f"{base_path}/{filename}") for key, filename in image_map.items()
    }

def get_shared_resources():
    return {
        "avatar": ft.Image(src="avatar.png", width=180, height=180, border_radius=90),
        "tech_images": load_images({
            "dotnet": "dotnet.png",
            "nodejs": "nodejs.png",
            "flet": "flet.png",
        }, "tech"),
        "flags_images": load_images({
            "uk": "uk_flag.png",
            "spain": "sp_flag.png",
            "italy": "it_flag.png",
            "germany": "de_flag.png",
        }, "flags"),
        "learning_images": load_images({
            "pluralsight": "pluralsight.png",
            "udemy": "udemy.png",
        }, "learning"),
        "city_images": load_images({
            "rosario": "rosario.jpg",
            "ilmenau": "ilmenau.jpg",
        }, "cities"),
        "companies_images": load_images({
            "softtek": "softtek.png",
            "acsys": "acsys.png",
            "sweatworks": "sweatworks.png",
            "tiarg": "tiarg.png",
            "globant": "globant.png",
            "tecso": "tecso.png",
            "utn": "utn.png",
        }, "experience"),
        "interest_images": load_images({
            "travelling": "travel.jpg",
            "vinyl": "vinyl.jpg",
            "music": "music.jpg",
            "sports": "sports.jpg",
            "photography": "photography.jpg",
            "art": "art.jpg",
            "cooking": "cooking.jpg",
            "datasci": "datasci.jpg",
        }, "interests")
    }

def main(page: ft.Page):
    is_dark = True
    def toggle_theme(e=None):
        nonlocal is_dark
        is_dark = not is_dark
        page.theme_mode = ft.ThemeMode.DARK if is_dark else ft.ThemeMode.LIGHT
        page.update()
    assets = get_shared_resources()
    def route_change(e):
        page.views.clear()
        route = page.route
        if route_view := NAV_ROUTES.get(route):
            match route:
                case "/":
                    route_view(page, toggle_theme, assets["avatar"])
                case "/projects":
                    route_view(page, toggle_theme, assets["tech_images"])
                case "/experience":
                    route_view(page, toggle_theme, assets["companies_images"])
                case "/education":
                    route_view(
                        page,
                        toggle_theme,
                        assets["flags_images"],
                        assets["learning_images"],
                        assets["city_images"]
                    )
                case "/interests":
                    route_view(page, toggle_theme, assets["interest_images"])
        page.update()
    page.on_route_change = route_change
    page.go(page.route or "/")

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")
