from rest_framework import serializers
from apps.security.Entity.models import Permission
from core.base.serializers.base_serializer import BaseSerializer

class PermissionSerializer(BaseSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'type_permission', 'description'] 
