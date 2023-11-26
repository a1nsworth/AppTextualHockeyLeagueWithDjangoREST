from typing import NoReturn

from rest_framework.viewsets import GenericViewSet
from rest_framework import routers


class SimpleRouterCreator:
    """

    """

    def __init__(self, name: str, view: GenericViewSet) -> NoReturn:
        self._route = routers.SimpleRouter()
        self._route.register(name, view)

    @property
    def urls(self) -> routers.BaseRouter:
        """

        Returns:

        """
        return self._route.urls
