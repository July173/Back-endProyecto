from core.base.Services.Implements.BaseService.BaseService import BaseService
from apps.Security.Repositories.FormRepository import FormRepository


class FormService(BaseService):
    def __init__(self):
        self.repository = FormRepository()
