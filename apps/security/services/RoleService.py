# apps/security/services/role_service.py
from core.base.services.base_service import BaseService
from apps.security.repositories.role_repository import RoleRepository

class RoleService(BaseService):
    def __init__(self):
        self.repository = RoleRepository()
