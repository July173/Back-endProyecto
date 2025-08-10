# core/base/controllers/base_viewset.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


class BaseViewSet(viewsets.ViewSet):
    service_class = None
    serializer_class = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.service_class:
            raise ValueError("Debe definir 'service_class'")
        if not self.serializer_class:
            raise ValueError("Debe definir 'serializer_class'")
        self.service = self.service_class()

    # --- NUEVO: requerido por drf-yasg y buena práctica DRF ---
    def get_serializer_class(self):
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        return self.get_serializer_class()(*args, **kwargs)
    # ----------------------------------------------------------

    def list(self, request):
        items = self.service.list()
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = self.service.get(pk)
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Usa service o serializer.save() según tu patrón:
        instance = self.service.create(serializer.validated_data)
        out = self.get_serializer(instance)
        return Response(out.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        instance = self.service.get(pk)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.service.update(pk, serializer.validated_data)
        out = self.get_serializer(instance)
        return Response(out.data)

    def partial_update(self, request, pk=None):
        instance = self.service.get(pk)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = self.service.update(pk, serializer.validated_data)
        out = self.get_serializer(instance)
        return Response(out.data)

    def destroy(self, request, pk=None):
        instance = self.service.get(pk)
        # Soft delete si el modelo expone is_deleted
        if hasattr(instance, "is_deleted"):
            instance.is_deleted = True
            instance.save()
        else:
            self.service.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['delete'], url_path='logical-delete')
    def logical_delete(self, request, pk=None):
        """
        Controlador para eliminación lógica (alterna activo/inactivo)
        URL: DELETE /api/recurso/1/logical-delete/
        """
        self.service.delete(pk, logical=True)
        return Response(
            {"message": "Estado del registro alternado correctamente"},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['delete'], url_path='persistential-delete')
    def persistential_delete(self, request, pk=None):
        """
        Controlador para eliminación persistencial (desactiva y guarda fecha)
        URL: DELETE /api/recurso/1/persistential-delete/
        """
        self.service.delete(pk, persistential=True)
        return Response(
            {"message": "Registro desactivado permanentemente con fecha"},
            status=status.HTTP_200_OK
        )
