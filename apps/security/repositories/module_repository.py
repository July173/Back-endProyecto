from core.base.repositories.base_repository import BaseRepository
from apps.security.Entity.models import Module

class ModuleRepository(BaseRepository):
    model = Module