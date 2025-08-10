from core.base.View.Implements import BaseViewSet
from apps.Security.Services.FormModuleService import FormModuleService
from apps.Security.Entity.Serializers.FormModuleSerializer import FormModuleSerializer


class FormModuleViewSet(BaseViewSet):
    service_class = FormModuleService
    serializer_class = FormModuleSerializer
