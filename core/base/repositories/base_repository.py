from django.utils import timezone

class BaseRepository:
    model = None

    def get_queryset(self):
        qs = self.model.objects.all()
        if hasattr(self.model, 'is_deleted'):
            qs = qs.filter(is_deleted=False)
        return qs

    def get_all(self):
        return self.get_queryset()

    def get_by_id(self, pk):
        return self.get_queryset().get(pk=pk)

    def create(self, data):
        return self.model.objects.create(**data)

    def update(self, instance, data):
        for k, v in data.items():
            setattr(instance, k, v)
        instance.save()
        return instance

    def persistential_delete(self, instance):
        """
        Eliminación persistencial: desactiva el registro y guarda la fecha.
        """
        # Desactivar el registro
        if hasattr(instance, 'active'):
            instance.active = False
        elif hasattr(instance, 'is_active'):
            instance.is_active = False
        elif hasattr(instance, 'is_deleted'):
            instance.is_deleted = True
        elif hasattr(instance, 'deleted'):
            instance.deleted = True
        
        # Guardar fecha de eliminación
        current_time = timezone.now()
        if hasattr(instance, 'delete_at'):
            instance.delete_at = current_time
        elif hasattr(instance, 'deleted_at'):
            instance.deleted_at = current_time
        elif hasattr(instance, 'date_deleted'):
            instance.date_deleted = current_time
        
        instance.save()
        return instance

    def logical_delete(self, instance):
        """
        Eliminación lógica: puede activar o desactivar según el estado actual.
        """
        # Toggle del estado activo
        if hasattr(instance, 'active'):
            instance.active = not instance.active
        elif hasattr(instance, 'is_active'):
            instance.is_active = not instance.is_active
        elif hasattr(instance, 'is_deleted'):
            instance.is_deleted = not instance.is_deleted
        elif hasattr(instance, 'deleted'):
            instance.deleted = not instance.deleted
        else:
            # Si no tiene campos de estado, hacer eliminación física
            instance.delete()
            return None
        
        instance.save()
        return instance

    def delete(self, instance):
        """
        Eliminación física permanente.
        """
        instance.delete()
        return None
