from rest_framework import serializers
from apps.security.Entity.models import Module
from core.base.serializers.base_serializer import BaseSerializer

class ModuleSerializer(BaseSerializer):
    class Meta:
        model = Module
        fields = ['id', 'name', 'description', 'active']
