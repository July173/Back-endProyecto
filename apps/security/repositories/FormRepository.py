from core.base.repositories.implements.base_repository.base_repository import BaseRepository
from apps.security.Entity.models import Form

class FormRepository(BaseRepository):
    model = Form