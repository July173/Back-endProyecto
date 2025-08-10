from core.base.View.Implements.BaseViewset import BaseViewSet
from apps.Security.Services.FormService import FormService
from apps.Security.Entity.Serializers.FormSerializer import FormSerializer


class FormViewSet(BaseViewSet):
    service_class = FormService
    serializer_class = FormSerializer
