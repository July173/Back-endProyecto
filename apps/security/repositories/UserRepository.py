from core.base.Repositories.Implements.BaseRepository import BaseRepository
from apps.Security.Entity.Models import User


class UserRepository(BaseRepository):
    model = User
