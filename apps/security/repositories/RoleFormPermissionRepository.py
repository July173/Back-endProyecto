from core.base.Repositories.Implements.BaseRepository import BaseRepository
from apps.Security.Entity.Models import RolFormPermission


class RolFormPermissionRepository(BaseRepository):
    model = RolFormPermission
