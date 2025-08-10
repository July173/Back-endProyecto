from core.base.Services.Implements.BaseService import BaseService
from apps.Security.Repositories.PerimissionRepository import PermissionRepository


class PermissionService(BaseService):
    def __init__(self):
        self.repository = PermissionRepository()