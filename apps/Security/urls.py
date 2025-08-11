# apps/security/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importa los ViewSets de todas las tablas
from apps.Security.Views.UserViewset import UserViewSet
from apps.Security.Views.RoleViewset import RoleViewSet
from apps.Security.Views.PersonViewset import PersonViewSet
from apps.Security.Views.FormViewset import FormViewSet
from apps.Security.Views.PermissionViewset import PermissionViewSet
from apps.Security.Views.ModuleViewset import ModuleViewSet
from apps.Security.Views.FormModuleViewset import FormModuleViewSet
from apps.Security.Views.RoleFormPermissionViewset import RolFormPermissionViewSet

# Importa login y refresh
from apps.Security.Views.auth_viewset import LoginView, RefreshView

# Configura el router y registra todos los ViewSets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'roles', RoleViewSet, basename='roles')
router.register(r'persons', PersonViewSet, basename='persons')
router.register(r'forms', FormViewSet, basename='forms')
router.register(r'permissions', PermissionViewSet, basename='permissions')
router.register(r'modules', ModuleViewSet, basename='modules')
router.register(r'form-modules', FormModuleViewSet, basename='form-modules')
router.register(r'rol-form-permissions', RolFormPermissionViewSet, basename='rol-form-permissions')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', RefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),  # Incluir las rutas del router
]
