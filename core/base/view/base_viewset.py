# core/base/controllers/base_viewset.py
from rest_framework import viewsets, status
from rest_framework.response import Response

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

    def list(self, request):
        items = self.service.list()
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = self.service.get(pk)
        serializer = self.serializer_class(item)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = self.service.create(serializer.validated_data)
        return Response(self.serializer_class(item).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = self.service.update(pk, serializer.validated_data)
        return Response(self.serializer_class(item).data)

    def partial_update(self, request, pk=None):
        serializer = self.serializer_class(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        item = self.service.update(pk, serializer.validated_data)
        return Response(self.serializer_class(item).data)

    def destroy(self, request, pk=None):
        instance = self.service.get(pk)
        # Soft delete si el modelo tiene el campo is_deleted
        if hasattr(instance, "is_deleted"):
            instance.is_deleted = True
            instance.save()
        else:
            self.service.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
