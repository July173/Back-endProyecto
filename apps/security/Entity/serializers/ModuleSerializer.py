from apps.Security.Entity.Models import Module
from core.base.Serializers.Implements.BaseSerializer import BaseSerializer


class ModuleSerializer(BaseSerializer):
    class Meta:
        model = Module
        fields = ['id', 'name', 'description', 'active']
