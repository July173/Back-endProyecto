from core.base.view.base_viewset import BaseViewSet
from apps.security.services.person_service import PersonService
from apps.security.Entity.serializers.person_serializer import PersonSerializer

class PersonViewSet(BaseViewSet):
    service_class = PersonService
    serializer_class = PersonSerializer