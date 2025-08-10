from apps.Security.Entity.Models import FormModule
from core.base.Serializers.Implements.BaseSerializer import BaseSerializer


class FormModuleSerializer(BaseSerializer):
    class Meta:
        model = FormModule
        fields = ['id', 'form', 'module', ]
