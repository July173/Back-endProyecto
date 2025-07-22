from core.base.repositories.base_repository import BaseRepository
from apps.security.Entity.models import User
class UserRepository(BaseRepository): model=User
