from core.base.Repositories.Implements.BaseRepository import BaseRepository
from apps.Security.Entity.Models import Module


class ModuleRepository(BaseRepository):
    model = Module
