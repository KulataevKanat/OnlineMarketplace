from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from api.models import Product
from api.serializers import ProductSerializers


class CreateProductView(generics.CreateAPIView):
    """Добавление товара"""

    serializer_class = ProductSerializers.CreateProductSerializer


class DeleteProductByIdView(generics.DestroyAPIView):
    """Удаления товара по идентификации"""

    queryset = Product.objects.all()


class DeleteAllProductView(generics.DestroyAPIView):
    """Удаление всех товаров"""

    def get_object(self):
        try:
            return Product.objects.all()
        except Product.DoesNotExist:
            raise Http404

    def delete(self, request, format=None, **kwargs):
        """Метод удаления всех товаров"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateProductByIdView(generics.UpdateAPIView):
    """Обновление товаров по идентификации"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers.UpdateProductSerializer


class GetProductView(generics.ListAPIView):
    """Вывод всех товаров"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers.GetProductSerializer


class FindProductByIdView(generics.RetrieveAPIView):
    """Поиск товара по идентификации"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializers.GetProductSerializer
