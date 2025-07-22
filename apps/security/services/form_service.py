from core.base.services.base_service import BaseService
from apps.security.repositories.form_repository import FormRepository

class FormService(BaseService):
    def __init__(self):
        self.repository = FormRepository()