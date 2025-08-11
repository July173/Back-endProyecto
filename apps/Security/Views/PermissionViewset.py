from core.base.View.Implements.BaseViewset import BaseViewSet
from apps.Security.Services.PermissionService import PermissionService
from apps.Security.Entity.Serializers.PermissionSerializer import PermissionSerializer


class PermissionViewSet(BaseViewSet):
    service_class = PermissionService
    serializer_class = PermissionSerializer
