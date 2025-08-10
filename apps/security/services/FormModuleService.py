from core.base.Services.Implements.BaseService.BaseService import BaseService
from apps.Security.Repositories.FormModuleRepository import FormModuleRepository


class FormModuleService(BaseService):
    def __init__(self):
        self.repository = FormModuleRepository()
