from core.base.Services.Implements.BaseService.BaseService import BaseService
from apps.Security.Repositories.ModuleRepository import ModuleRepository


class ModuleService(BaseService):
    def __init__(self):
        self.repository = ModuleRepository()
