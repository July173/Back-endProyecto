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
        for k, v in data.items(): setattr(instance, k, v)
        instance.save(); return instance

    def logical_delete(self, instance):
        if hasattr(instance, 'is_deleted'):
            instance. is_deleted = True; instance.save(); return instance
        instance.delete(); return None

    def delete(self, instance):
        instance.delete(); return None
