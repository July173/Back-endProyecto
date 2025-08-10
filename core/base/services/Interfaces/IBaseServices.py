# core/base/services/interfaces.py
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")


class IBaseService(ABC, Generic[T]):
    """Interfaz base para servicios."""

    @abstractmethod
    def list(self) -> List[T]:
        pass

    @abstractmethod
    def get(self, id: int) -> Optional[T]:
        pass

    @abstractmethod
    def create(self, data: dict) -> T:
        pass

    @abstractmethod
    def update(self, id: int, data: dict) -> T:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
