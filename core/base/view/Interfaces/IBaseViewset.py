# core/base/view/interfaces.py
from abc import ABC, abstractmethod
from rest_framework.request import Request
from rest_framework.response import Response


class IBaseViewSet(ABC):
    """Interfaz para ViewSets personalizados."""

    @abstractmethod
    def list(self, request: Request) -> Response:
        pass

    @abstractmethod
    def retrieve(self, request: Request, pk=None) -> Response:
        pass

    @abstractmethod
    def create(self, request: Request) -> Response:
        pass

    @abstractmethod
    def update(self, request: Request, pk=None) -> Response:
        pass

    @abstractmethod
    def destroy(self, request: Request, pk=None) -> Response:
        pass
