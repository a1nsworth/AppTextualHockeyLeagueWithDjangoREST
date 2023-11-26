from textual import app
from textual.app import ComposeResult
from textual.widgets import Header, Footer

import tabs


class Application(app.App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield tabs.MainTabContent()


if __name__ == '__main__':
    Application().run()
