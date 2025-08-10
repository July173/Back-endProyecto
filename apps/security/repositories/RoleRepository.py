from core.base.Repositories.Implements.BaseRepository.BaseRepository import BaseRepository
from apps.Security.Entity.Models import Role


class RoleRepository(BaseRepository):
    model = Role
