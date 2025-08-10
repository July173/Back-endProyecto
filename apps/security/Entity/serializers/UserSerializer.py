from rest_framework import serializers
from apps.security.Entity.models import User
from core.base.serializers.base_serializer import BaseSerializer
class UserSerializer(BaseSerializer):
  class Meta:
        model = User
        fields = ['email', 'password', 'person', 'role']
