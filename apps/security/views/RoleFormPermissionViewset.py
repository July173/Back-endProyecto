from core.base.view.base_viewset import BaseViewSet
from apps.security.services.rol_form_permission_service import RolFormPermissionService
from apps.security.Entity.serializers.rol_form_permission_serializer import RolFormPermissionSerializer

class RolFormPermissionViewSet(BaseViewSet):
    service_class = RolFormPermissionService
    serializer_class = RolFormPermissionSerializer