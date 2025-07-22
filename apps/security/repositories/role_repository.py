from core.base.repositories.base_repository import BaseRepository
from apps.security.Entity.models import Role
class RoleRepository(BaseRepository):
    model = Role
