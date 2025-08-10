from core.base.services.base_service import BaseService
from apps.security.repositories.person_repository import PersonRepository

class PersonService(BaseService):
    def __init__(self):
        self.repository = PersonRepository()