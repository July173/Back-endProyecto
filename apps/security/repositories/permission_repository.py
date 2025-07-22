from core.base.repositories.base_repository import BaseRepository
from apps.security.Entity.models import Permission

class PermissionRepository(BaseRepository):
    model = Permission