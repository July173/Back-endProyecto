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
        # Debug: Mostrar campos disponibles
        print(f"Modelo: {instance.__class__.__name__}")
        print(f"Campos disponibles: {[field.name for field in instance._meta.fields]}")
        
        # Desactivar el registro
        if hasattr(instance, 'active'):
            print(f"Campo 'active' encontrado. Valor actual: {instance.active}")
            instance.active = False
            print(f"Campo 'active' cambiado a: {instance.active}")
        elif hasattr(instance, 'is_active'):
            print(f"Campo 'is_active' encontrado. Valor actual: {instance.is_active}")
            instance.is_active = False
            print(f"Campo 'is_active' cambiado a: {instance.is_active}")
        elif hasattr(instance, 'is_deleted'):
            print(f"Campo 'is_deleted' encontrado. Valor actual: {instance.is_deleted}")
            instance.is_deleted = True
            print(f"Campo 'is_deleted' cambiado a: {instance.is_deleted}")
        elif hasattr(instance, 'deleted'):
            print(f"Campo 'deleted' encontrado. Valor actual: {instance.deleted}")
            instance.deleted = True
            print(f"Campo 'deleted' cambiado a: {instance.deleted}")
        
        # Guardar fecha de eliminación
        current_time = timezone.now()
        print(f"Fecha actual: {current_time}")
        
        if hasattr(instance, 'delete_at'):
            print(f"Campo 'delete_at' encontrado. Valor actual: {instance.delete_at}")
            instance.delete_at = current_time
            print(f"Campo 'delete_at' cambiado a: {instance.delete_at}")
        elif hasattr(instance, 'deleted_at'):
            print(f"Campo 'deleted_at' encontrado. Valor actual: {instance.deleted_at}")
            instance.deleted_at = current_time
            print(f"Campo 'deleted_at' cambiado a: {instance.deleted_at}")
        elif hasattr(instance, 'date_deleted'):
            print(f"Campo 'date_deleted' encontrado. Valor actual: {instance.date_deleted}")
            instance.date_deleted = current_time
            print(f"Campo 'date_deleted' cambiado a: {instance.date_deleted}")
        else:
            print("¡ADVERTENCIA! No se encontró ningún campo de fecha de eliminación")
        
        print("Guardando instancia...")
        instance.save()
        print("Instancia guardada")
        
        # Verificar que se guardó correctamente
        instance.refresh_from_db()
        print(f"Después de guardar - active: {getattr(instance, 'active', 'N/A')}")
        print(f"Después de guardar - delete_at: {getattr(instance, 'delete_at', 'N/A')}")
        
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
