from apps.Security.Entity.Models import RolFormPermission
from core.base.Serializers.Implements.BaseSerializer.BaseSerializer import BaseSerializer


class RolFormPermissionSerializer(BaseSerializer):
    class Meta:
        model = RolFormPermission
        fields = ['id', 'role', 'form', 'permission']
