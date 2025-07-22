from core.base.view.base_viewset import BaseViewSet
from apps.security.services.form_service import FormService
from apps.security.Entity.serializers.form_serializer import FormSerializer

class FormViewSet(BaseViewSet):
    service_class = FormService
    serializer_class = FormSerializer