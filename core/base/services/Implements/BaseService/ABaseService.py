from abc import ABC
from typing import TypeVar, List, Optional, Dict, Any
from core.base.Services.Interfaces import IBaseService
from core.base.Repositories.Interfaces.IBaseRepository import IBaseRepository

T = TypeVar("T")


class AbstractBaseService(IBaseService[T], ABC):
    """Implementación base abstracta del servicio."""

    def __init__(self, repository: IBaseRepository[T]):
        self.repository = repository

    def list(self) -> List[T]:
        return self.repository.get_all()

    def get(self, id: int) -> Optional[T]:
        return self.repository.get_by_id(id)

    def create(self, data: Dict[str, Any]) -> T:
        # Dejamos la implementación concreta para las clases hijas
        # ya que puede variar según el modelo
        raise NotImplementedError("El método create debe ser implementado en la clase concreta")

    def update(self, id: int, data: Dict[str, Any]) -> T:
        instance = self.get(id)
        if instance is None:
            raise ValueError(f"Instancia con id {id} no encontrada")

        for key, value in data.items():
            setattr(instance, key, value)
        return self.repository.update(instance)

    def delete(self, id: int) -> bool:
        return self.repository.delete(id)
