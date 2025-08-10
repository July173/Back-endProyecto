from core.base.Repositories.Implements.BaseRepository import BaseRepository
from apps.Security.Entity.Models import FormModule


class FormModuleRepository(BaseRepository):
    model = FormModule
