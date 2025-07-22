# apps/security/models.py
from apps.security.Entity.models.user import User
from apps.security.Entity.models.role import Role  # o Role si así se llama
from apps.security.Entity.models.person import Person
from apps.security.Entity.models.form import Form
from apps.security.Entity.models.permission import Permission
from apps.security.Entity.models.module import Module
from apps.security.Entity.models.form_module import FormModule
from apps.security.Entity.models.rol_form_permission import RolFormPermission
