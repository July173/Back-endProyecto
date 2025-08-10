from core.base.Repositories.Implements.BaseRepository.BaseRepository import BaseRepository
from apps.Security.Entity.Models import FormModule


class FormModuleRepository(BaseRepository):
    model = FormModule
