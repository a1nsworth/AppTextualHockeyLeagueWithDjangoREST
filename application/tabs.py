from typing import Any

from textual import events
from textual.app import ComposeResult
from textual.widgets import TabbedContent, TabPane, DataTable, Select, Button, Input
import requests
import parser

PARSER = parser.Parser()


class GetTab(TabPane):
    ALL_GET_URLS = PARSER.all_get_urls()

    def compose(self) -> ComposeResult:
        yield DataTable(id='table_get_response')
        yield Select(options=[(request_url, request_url) for request_url in GetTab.ALL_GET_URLS])
        yield Button()

    def on_mount(self, event: events.Mount) -> None:
        event.prevent_default(False)

        table = self.query_one('#table_get_response', DataTable)
        r = requests.get(parser.API_URL + GetTab.ALL_GET_URLS[0])
        json: list[dict[str, Any]] = r.json()
        table.add_column(*list(json[0].keys()))
        for d in json:
            table.add_row(*list(d.values()))


class RetrieveTab(TabPane):
    def compose(self) -> ComposeResult:
        yield Select(
            options=[(request_url, request_url) for request_url in PARSER.all_get_by_key_urls()])
        yield Input()
        yield Button()


class MainTabContent(TabbedContent):
    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield GetTab(title='GET Запросы')
            yield RetrieveTab(title='GET Запросы по ключу')
