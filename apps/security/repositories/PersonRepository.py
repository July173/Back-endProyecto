from core.base.Repositories.Implements.BaseRepository import BaseRepository
from apps.Security.Entity.Models import Person


class PersonRepository(BaseRepository):
    model = Person
