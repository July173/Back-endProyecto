from rest_framework import serializers
from apps.security.Entity.models import Form
from core.base.serializers.base_serializer import BaseSerializer

class FormSerializer(BaseSerializer):
    class Meta:
        model = Form
        fields = '__all__'
