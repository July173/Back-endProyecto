from core.base.View.Implements.BaseViewset import BaseViewSet
from apps.Security.Services.ModuleService import ModuleService
from apps.Security.Entity.Serializers.ModuleSerializer import ModuleSerializer


class ModuleViewSet(BaseViewSet):
    service_class = ModuleService
    serializer_class = ModuleSerializer
