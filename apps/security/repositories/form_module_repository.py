from core.base.repositories.base_repository import BaseRepository
from apps.security.Entity.models import FormModule

class FormModuleRepository(BaseRepository):
    model = FormModule