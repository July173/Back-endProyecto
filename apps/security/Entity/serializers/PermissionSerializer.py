from apps.Security.Entity.Models import Permission
from core.base.Serializers.Implements.BaseSerializer import BaseSerializer


class PermissionSerializer(BaseSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'type_permission', 'description']
