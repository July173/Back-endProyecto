from core.base.Repositories.Implements.BaseRepository.BaseRepository import BaseRepository
from apps.Security.Entity.Models import Module


class ModuleRepository(BaseRepository):
    model = Module
