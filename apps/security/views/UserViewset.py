from core.base.View.Implements import BaseViewSet
from apps.Security.Services.UserService import UserService
from apps.Security.Entity.Serializers.UserSerializer import UserSerializer


class UserViewSet(BaseViewSet):
    service_class = UserService
    serializer_class = UserSerializer
