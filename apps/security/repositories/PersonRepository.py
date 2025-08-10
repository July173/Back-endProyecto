from core.base.Repositories.Implements.BaseRepository.BaseRepository import BaseRepository
from apps.Security.Entity.Models import Person


class PersonRepository(BaseRepository):
    model = Person
