from core.base.services.base_service import BaseService
from apps.security.repositories.permission_repository import PermissionRepository

class PermissionService(BaseService):
    def __init__(self):
        self.repository = PermissionRepository()