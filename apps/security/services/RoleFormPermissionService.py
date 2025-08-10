from core.base.Services.Implements.BaseService.BaseService import BaseService
from apps.Security.Repositories.RoleFormPermissionRepository import RolFormPermissionRepository


class RolFormPermissionService(BaseService):
    def __init__(self):
        self.repository = RolFormPermissionRepository()
