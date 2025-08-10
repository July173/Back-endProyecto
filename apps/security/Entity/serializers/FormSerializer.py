from apps.Security.Entity.Models import Form
from core.base.Serializers.Implements.BaseSerializer import BaseSerializer


class FormSerializer(BaseSerializer):
    class Meta:
        model = Form
        fields = ['id', 'name', 'description', 'active']
