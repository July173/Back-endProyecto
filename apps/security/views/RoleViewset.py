from core.base.View.Implements.BaseViewset import BaseViewSet
from apps.Security.Services.RoleService import RoleService
from apps.Security.Entity.Serializers.RoleSerializer import RoleSerializer


class RoleViewSet(BaseViewSet):
    service_class = RoleService
    serializer_class = RoleSerializer
