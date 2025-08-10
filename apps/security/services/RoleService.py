# apps/security/services/role_service.py
from core.base.Services.Implements.BaseService.BaseService import BaseService
from apps.Security.Repositories.RoleRepository import RoleRepository


class RoleService(BaseService):
    def __init__(self):
        self.repository = RoleRepository()
