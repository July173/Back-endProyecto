from apps.Security.Entity.Models import Role
from core.base.Serializers.Implements.BaseSerializer import BaseSerializer


class RoleSerializer(BaseSerializer):
    class Meta:
        model = Role
        fields = ['id', 'type_role', 'description', 'active']
