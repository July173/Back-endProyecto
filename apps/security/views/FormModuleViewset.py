from core.base.view.base_viewset import BaseViewSet
from apps.security.services.form_module_service import FormModuleService
from apps.security.Entity.serializers.form_module_serializer import FormModuleSerializer

class FormModuleViewSet(BaseViewSet):
    service_class = FormModuleService
    serializer_class = FormModuleSerializer