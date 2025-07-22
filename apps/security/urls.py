# apps/security/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importa los ViewSets de todas las tablas
from apps.security.views.user_viewset import UserViewSet
from apps.security.views.role_viewset import RoleViewSet
from apps.security.views.person_viewset import PersonViewSet
from apps.security.views.form_viewset import FormViewSet
from apps.security.views.permission_viewset import PermissionViewSet
from apps.security.views.module_viewset import ModuleViewSet
from apps.security.views.form_module_viewset import FormModuleViewSet
from apps.security.views.rol_form_permission_viewset import RolFormPermissionViewSet

# Importa login y refresh
from apps.security.views.auth_viewset import LoginView, RefreshView

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
