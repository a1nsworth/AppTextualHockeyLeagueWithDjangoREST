from textual.app import ComposeResult, App
from textual.widgets import Header, Footer

import tabs


class Application(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield tabs.MainTabContent()


if __name__ == '__main__':
    Application().run()
