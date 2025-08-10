from core.base.View.Implements import BaseViewSet
from apps.Security.Services.PersonService import PersonService
from apps.Security.Entity.Serializers.PersonSerializer import PersonSerializer


class PersonViewSet(BaseViewSet):
    service_class = PersonService
    serializer_class = PersonSerializer
