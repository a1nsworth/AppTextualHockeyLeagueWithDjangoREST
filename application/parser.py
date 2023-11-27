from typing import Any

import requests

BASE_URL = 'http://127.0.0.1:8000/'
API_URL = BASE_URL + 'api/v1'
DOC_URL = API_URL + '/swagger/schema/?format=openapi'


class Parser:
    """

    """

    def __init__(self):
        self._request = requests.get(DOC_URL)
        self._json: dict[str, Any] = self._request.json()

    @property
    def request(self):
        return self._request

    @property
    def json(self) -> dict[str, Any]:
        return self._json

    def all_get_urls(self):
        """

        Returns:
            Все url по которым доступен GET метод без ключа

        """
        return [path for path in self._json['paths'].keys() if
                len(list(self._json['paths'][path]['parameters'])) == 0]

    def all_get_by_key_urls(self):
        """

        Returns:
            Все url по которым доступен GET метод c ключем

        """
        return [path for path in self._json['paths'].keys() if
                len(list(self._json['paths'][path]['parameters'])) != 0]
