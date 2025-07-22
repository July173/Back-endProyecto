from rest_framework import serializers
from apps.security.Entity.models.role import Role
from core.base.serializers.base_serializer import BaseSerializer
class RoleSerializer(BaseSerializer):
    class Meta: 
        model=Role; 
        fields=['id','type_role','description']
