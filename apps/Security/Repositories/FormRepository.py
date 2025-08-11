from core.base.Repositories.Implements.BaseRepository.BaseRepository import BaseRepository
from apps.Security.Entity.Models import Form


class FormRepository(BaseRepository):
    def __init__(self):
        super().__init__(Form)
