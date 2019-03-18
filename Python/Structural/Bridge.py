import abc


class Theme(abc.ABC):
    @abc.abstractmethod
    def get_color(self) -> str:
        pass


class DarkTheme(Theme):
    def get_color(self):
        return 'Dark Black'


class LightTheme(Theme):
    def get_color(self):
        return 'Off White'


class AquaTheme(Theme):
    def get_color(self):
        return 'Light Blue'


class WebPage:
    def __init__(self, name: str, theme: Theme):
        self._name = name
        self._theme = theme

    def get_content(self):
        return f'{self._name} page in {self._theme.get_color()}'


class AboutPage(WebPage):
    def __init__(self, theme: Theme):
        super().__init__('About', theme)


class CareersPage(WebPage):
    def __init__(self, theme: Theme):
        super().__init__('Careers', theme)


if __name__ == '__main__':
    # Create two lists of all theme and page classes
    themes = [DarkTheme, LightTheme, AquaTheme]
    pages = [AboutPage, CareersPage]

    # Loop through all theme classes
    for theme_class in themes:
        # Create a new instance of the theme
        theme = theme_class()

        # Loop through all pages classes
        for page_class in pages:
            # Create a new instance of the page
            page = page_class(theme)

            # Output the page content to console
            print(page.get_content())
