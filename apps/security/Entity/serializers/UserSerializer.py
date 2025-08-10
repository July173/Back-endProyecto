from apps.Security.Entity.Models import User
from core.base.Serializers.Implements.BaseSerializer import BaseSerializer


class UserSerializer(BaseSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'person', 'role']
