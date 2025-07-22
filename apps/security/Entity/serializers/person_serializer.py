from rest_framework import serializers
from apps.security.Entity.models import Person
from core.base.serializers.base_serializer import BaseSerializer

class PersonSerializer(BaseSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'active']
