# core/base/repositories/base_repository.py
from abc import ABC
from django.db import models
from typing import TypeVar, List, Optional
from core.base.Repositories.Interfaces import IBaseRepository

T = TypeVar("T", bound=models.Model)


class AbstractBaseRepository(IBaseRepository[T], ABC):
    """Implementación parcial de la interfaz del repositorio."""

    def _init_(self, model: type[T]):
        self.model = model

    def get_all(self) -> List[T]:
        return list(self.model.objects.all())

    def get_by_id(self, id: int) -> Optional[T]:
        return self.model.objects.filter(pk=id).first()

    def create(self, entity: T) -> T:
        entity.save()
        return entity

    def update(self, entity: T) -> T:
        entity.save()
        return entity

    def delete(self, id: int) -> bool:
        obj = self.get_by_id(id)
        if obj:
            obj.delete()
            return True
        return False
