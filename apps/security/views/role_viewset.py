
from core.base.view.base_viewset import BaseViewSet
from apps.security.services.role_service import RoleService, RoleService
from apps.security.Entity.serializers.role_serializer import RoleSerializer

class RoleViewSet(BaseViewSet):
    service_class = RoleService
    serializer_class = RoleSerializer
