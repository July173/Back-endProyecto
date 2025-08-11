from core.base.Repositories.Implements.BaseRepository.BaseRepository import BaseRepository
from apps.Security.Entity.Models import User


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)
