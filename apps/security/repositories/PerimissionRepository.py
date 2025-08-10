from core.base.Repositories.Implements.BaseRepository.BaseRepository import BaseRepository
from apps.Security.Entity.Models import Permission


class PermissionRepository(BaseRepository):
    model = Permission
