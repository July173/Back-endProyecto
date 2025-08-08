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

    def logical_delete(self, instance):
        """
        Realiza eliminación lógica desactivando el registro.
        Busca campos como 'is_active', 'active', 'is_deleted' o 'deleted'.
        """
        if hasattr(instance, 'is_active'):
            instance.is_active = False
        elif hasattr(instance, 'active'):
            instance.active = False
        elif hasattr(instance, 'is_deleted'):
            instance.is_deleted = True
        elif hasattr(instance, 'deleted'):
            instance.deleted = True
        else:
            # Si no tiene campos de estado, hacer eliminación física
            instance.delete()
            return None
        
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return None
