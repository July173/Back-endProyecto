from core.base.View.Implements.BaseViewset import BaseViewSet
from apps.Security.Services.RoleFormPermissionService import RolFormPermissionService
from apps.Security.Entity.Serializers.RoleFormPermissionSerializer import RolFormPermissionSerializer


class RolFormPermissionViewSet(BaseViewSet):
    service_class = RolFormPermissionService
    serializer_class = RolFormPermissionSerializer
