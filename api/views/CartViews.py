from rest_framework import generics

from api.models import Cart
from api.serializers import CartSerializers


class CreateCartView(generics.CreateAPIView):
    """Добавление товара в корзину"""

    serializer_class = CartSerializers.CreateCartSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteCartByIdView(generics.DestroyAPIView):
    """Удаление товара из корзины по идентификации"""

    queryset = Cart.objects.all()


class UpdateCartByIdView(generics.UpdateAPIView):
    """Обновление товара из корзины по идентификации"""

    queryset = Cart.objects.all()
    serializer_class = CartSerializers.UpdateCartSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class GetCartView(generics.ListAPIView):
    """Вывод товаров из корзины"""

    queryset = Cart.objects.all()
    serializer_class = CartSerializers.GetCartSerializer


class FindCartByIdView(generics.RetrieveAPIView):
    """Поиск товаров из корзины по идентификации"""

    queryset = Cart.objects.all()
    serializer_class = CartSerializers.GetCartSerializer
