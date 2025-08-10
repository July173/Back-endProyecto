class BaseService:
    repository = None

    def list(self):
        return self.repository.get_all()

    def get(self, pk):
        return self.repository.get_by_id(pk)

    def create(self, data):
        return self.repository.create(data)

    def update(self, pk, data):
        inst = self.get(pk)
        return self.repository.update(inst, data)

    def persistential_delete(self, pk):
        """
        Eliminación persistencial: desactiva el registro y guarda fecha.

        Args:
            pk: ID del registro a eliminar

        Returns:
            La instancia modificada con estado desactivado
        """
        inst = self.get(pk)
        return self.repository.persistential_delete(inst)

    def logical_delete(self, pk):
        """
        Eliminación lógica: alterna entre activar/desactivar.

        Args:
            pk: ID del registro a modificar

        Returns:
            La instancia modificada con estado alternado
        """
        inst = self.get(pk)
        return self.repository.logical_delete(inst)

    def delete(self, pk, delete_type='logical', logical=None, persistential=None, physical=None):
        """
        Elimina un registro por su ID según el tipo especificado.

        Args:
            pk: ID del registro a eliminar
            delete_type (str): 'logical', 'persistential' o 'physical'
            logical (bool): Si es True, hace eliminación lógica (compatibilidad)
            persistential (bool): Si es True, hace eliminación persistencial (compatibilidad)
            physical (bool): Si es True, hace eliminación física (compatibilidad)

        Returns:
            La instancia modificada o None (eliminación física)
        """
        # Manejar parámetros de compatibilidad
        if logical is True:
            delete_type = 'logical'
        elif persistential is True:
            delete_type = 'persistential'
        elif physical is True:
            delete_type = 'physical'

        inst = self.get(pk)

        if delete_type == 'persistential':
            return self.repository.persistential_delete(inst)
        elif delete_type == 'logical':
            return self.repository.logical_delete(inst)
        elif delete_type == 'physical':
            return self.repository.delete(inst)
        else:
            raise ValueError("delete_type debe ser 'logical', 'persistential' o 'physical'")
