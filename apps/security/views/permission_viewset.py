from core.base.view.base_viewset import BaseViewSet
from apps.security.services.permission_service import PermissionService
from apps.security.Entity.serializers.permission_serializer import PermissionSerializer

class PermissionViewSet(BaseViewSet):
    service_class = PermissionService
    serializer_class = PermissionSerializer