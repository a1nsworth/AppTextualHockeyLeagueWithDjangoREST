from typing import Any

from textual import events, on
from textual import events
from textual.app import ComposeResult
from textual.containers import Horizontal, Container, Center
from textual.widgets import TabbedContent, TabPane, DataTable, Select, Button, Input
import requests
import parser

PARSER = parser.Parser()
ALL_GET_URLS = PARSER.all_get_urls()
ALL_GET_BY_KEY_URLS = PARSER.all_get_by_key_urls()


def update_table_from_json(table: DataTable, json: list[dict[str, Any]] | dict[str, Any], columns: bool = True):
    """
    Очищает и заполняет таблицу новыми данными.

    Args:
        table: таблица.
        json: данные для заполнения.
        columns: при очистке таблицы, сохранять ли столбцы.

    Returns:
        None
    """
    table.clear(columns)

    if isinstance(json, list):
        if len(json) > 0 and isinstance(json[0], dict):
            table.add_columns(*list(json[0].keys()))
            for record in json:
                table.add_row(*list(record.values()))
    elif isinstance(json, dict):
        table.add_columns(*list(json.keys()))
        table.add_row(*list(json.values()))


class GetTab(TabPane):
    """
    Страница.
    """

    DEFAULT_CSS = """
    #container_tab_get_response {
        layout: grid;
        grid-size: 2;
    }
    
    #table_get_response {
        width: auto;
        height: auto;
    }
    """

    def compose(self) -> ComposeResult:
        with Container(id='container_tab_get_response'):
            with Container(id='container_table_get_response'):
                yield DataTable(id='table_get_response', zebra_stripes=True)
            with Container():
                yield Select(id='select_get_request',
                             options=[(request_url, i) for i, request_url in enumerate(ALL_GET_URLS)],
                             prompt='Select GET request',
                             )
                with Center():
                    yield Button(id='button_update_get_table', label='Update Table')

    def on_mount(self, event: events.Mount) -> None:
        event.prevent_default(False)
        update_table_from_json(self.query_one('#table_get_response', DataTable),
                               requests.get(parser.API_URL + ALL_GET_URLS[0]).json())

    @on(Button.Pressed, '#button_update_get_table')
    def update_table(self):
        """
        Обновляет таблицу при нажатии на кнопку.

        Returns:
            None
        """
        selected_value = self.query_one('#select_get_request', Select).value

        if selected_value != Select.BLANK:
            table = self.query_one('#table_get_response', DataTable)
            json: list[dict[str, Any]] = requests.get(parser.API_URL + ALL_GET_URLS[selected_value]).json()
            update_table_from_json(table, json)


class RetrieveTab(TabPane):
    """
    Страница
    """

    DEFAULT_CSS = """
    #container_tab_retrieve_response {
        layout: grid;
        grid-size: 2;
        grid-columns: 1fr;
        grid-rows: 1fr;
    }
    
    #container_table_retrieve_response {
        row-span: 2;
    }
    
    #table_retrieve_response {
        width: 100%;
        height: 100%;
    }
    
    #container_select_input_retrieve {
        layout: grid;
        height: auto;
        grid-size: 2;
    }
    
    
    #container_button_update_retrieve_table {
        align: center top;
        width: 100%;
        height: auto;
    }
    
    #button_update_retrieve_table {
    }
    """

    def compose(self) -> ComposeResult:
        with Container(id='container_tab_retrieve_response'):
            with Container(id='container_table_retrieve_response'):
                yield DataTable(id='table_retrieve_response', zebra_stripes=True)
            with Container(id='container_select_input_retrieve'):
                yield Select(id='select_retrieve_request',
                             options=[(request_url, i) for i, request_url in enumerate(ALL_GET_BY_KEY_URLS)],
                             prompt='Select GET request by {key}',
                             )
                yield Input(id='input_key_retrieve_request', placeholder='Enter key')
            with Container(id='container_button_update_retrieve_table'):
                yield Button(id='button_update_retrieve_table', label='Update Table')

    def on_mount(self, event: events.Mount) -> None:
        event.prevent_default(False)
        update_table_from_json(self.query_one('#table_retrieve_response', DataTable),
                               requests.get(parser.API_URL + ALL_GET_URLS[0]).json())

    @on(events.Key)
    def update_table_pressed_enter(self, event: events.Key):
        if event.key == 'enter':
            self.update_table()

    @on(Button.Pressed, '#button_update_retrieve_table')
    def update_table(self):
        selected_request = self.query_one('#select_retrieve_request', Select).value
        key = self.query_one('#input_key_retrieve_request', Input).value

        if selected_request != Select.BLANK and key:
            table = self.query_one('#table_retrieve_response', DataTable)
            json: dict[str, Any] = requests.get(
                parser.API_URL + ALL_GET_URLS[selected_request] + key + '/').json()
            update_table_from_json(table, json)


class MainTabContent(TabbedContent):
    """
    Страницы приложения.
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield GetTab(title='GET Requests')
            yield RetrieveTab(title='GET Requests by {key}')
