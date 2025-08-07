class BaseService:
    repository = None

    def list(self): return self.repository.get_all()

    def get(self, pk): return self.repository.get_by_id(pk)

    def create(self, data): return self.repository.create(data)

    def update(self, pk, data):
        inst = self.get(pk);
        return self.repository.update(inst, data)

    def delete(self, pk, logical=True):
        inst = self.get(pk)
        return self.repository.logical_delete(inst) if logical else self.repository.delete(inst)
