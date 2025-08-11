from core.base.Repositories.Implements.BaseRepository.BaseRepository import BaseRepository
from apps.Security.Entity.Models import RolFormPermission


class RolFormPermissionRepository(BaseRepository):
    def __init__(self):
        super().__init__(RolFormPermission)
