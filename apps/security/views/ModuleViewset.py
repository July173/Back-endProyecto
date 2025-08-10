from core.base.view.base_viewset import BaseViewSet
from apps.security.services.module_service import ModuleService
from apps.security.Entity.serializers.module_serializer import ModuleSerializer

class ModuleViewSet(BaseViewSet):
    service_class = ModuleService
    serializer_class = ModuleSerializer