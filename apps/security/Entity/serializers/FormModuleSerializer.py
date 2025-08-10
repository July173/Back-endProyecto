from rest_framework import serializers
from apps.security.Entity.models import FormModule
from core.base.serializers.base_serializer import BaseSerializer

class FormModuleSerializer(BaseSerializer):
    class Meta:
        model = FormModule
        fields = ['id', 'form', 'module', ]
