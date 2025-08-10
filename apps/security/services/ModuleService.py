from core.base.services.base_service import BaseService
from apps.security.repositories.module_repository import ModuleRepository

class ModuleService(BaseService):
    def __init__(self):
        self.repository = ModuleRepository()