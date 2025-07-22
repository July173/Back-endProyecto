from core.base.services.base_service import BaseService
from apps.security.repositories.rol_form_permission_repository import RolFormPermissionRepository

class RolFormPermissionService(BaseService):
    def __init__(self):
        self.repository = RolFormPermissionRepository()