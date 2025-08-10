# core/base/services/base_service.py
from abc import ABC
from typing import TypeVar, List, Optional
from core.base.Services.Interfaces import IBaseService
from core.base.Repositories.Interfaces import IBaseRepository

T = TypeVar("T")


class AbstractBaseService(IBaseService[T], ABC):
    """Implementación base que usa un repositorio."""

    def _init_(self, repository: IBaseRepository[T]):
        self.repository = repository

    def list(self) -> List[T]:
        return self.repository.get_all()

    def get(self, id: int) -> Optional[T]:
        return self.repository.get_by_id(id)

    def create(self, data: dict) -> T:
        instance = self.repository.model(**data)
        return self.repository.create(instance)

    def update(self, id: int, data: dict) -> T:
        instance = self.repository.get_by_id(id)
        for key, value in data.items():
            setattr(instance, key, value)
        return self.repository.update(instance)

    def delete(self, id: int) -> bool:
        return self.repository.delete(id)
