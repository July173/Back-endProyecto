from core.base.services.base_service import BaseService
from apps.security.repositories.form_module_repository import FormModuleRepository

class FormModuleService(BaseService):
    def __init__(self):
        self.repository = FormModuleRepository()