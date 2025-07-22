# apps/security/controllers/user_controller.py
from core.base.view.base_viewset import BaseViewSet
from apps.security.services.user_service import UserService
from apps.security.Entity.serializers.user_serializer import UserSerializer

class UserViewSet(BaseViewSet):
    service_class = UserService
    serializer_class = UserSerializer
