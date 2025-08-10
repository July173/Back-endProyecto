from core.base.Services.Implements.BaseService import BaseService
from apps.Security.Repositories.PersonRepository import PersonRepository


class PersonService(BaseService):
    def __init__(self):
        self.repository = PersonRepository()
