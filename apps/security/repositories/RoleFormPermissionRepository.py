from core.base.Repositories.Implements.BaseRepository.BaseRepository import BaseRepository
from apps.Security.Entity.Models import RolFormPermission


class RolFormPermissionRepository(BaseRepository):
    model = RolFormPermission
