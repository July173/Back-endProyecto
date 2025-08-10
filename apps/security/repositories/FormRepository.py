from core.base.Repositories.Implements.BaseRepository.BaseRepository import BaseRepository
from apps.Security.Entity.Models import Form


class FormRepository(BaseRepository):
    model = Form
