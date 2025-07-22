from rest_framework import serializers
from apps.security.Entity.models import RolFormPermission
from core.base.serializers.base_serializer import BaseSerializer

class RolFormPermissionSerializer(BaseSerializer):
    class Meta:
        model = RolFormPermission
        fields = '__all__'
