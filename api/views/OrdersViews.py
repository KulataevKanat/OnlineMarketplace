from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response

from OnlineMarketplace.advice import PURCHASED
from api.models import Cart, Orders
from api.serializers import OrdersSerializers


class CreateOrderView(generics.CreateAPIView):
    """Добавление заказа"""

    serializer_class = OrdersSerializers.CreateOrderSerializer

    def post(self, request, *args, **kwargs):
        """Метод добавление заказа"""

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            for product_history, product in zip(request.data['product_history'], Cart.objects.all()):
                product_history['prod_id'] = product.product_id.id
                product_history['title'] = product.product_id.title
                product_history['description'] = product.product_id.description
                product_history['amount'] = product.amount
                if product_history['price'].__eq__(int()):
                    product_history['price'] = product.product_id.price
                    self.perform_create(serializer, product)
                else:
                    self.perform_create(serializer, product)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer, product=None):
        serializer.save(
            client_id=self.request.user,
            status=PURCHASED
        )
        product.delete()


class DeleteOrderByIdView(generics.DestroyAPIView):
    """Удаление заказа по идентификации"""

    queryset = Orders.objects.all()


class DeleteAllOrdersView(generics.DestroyAPIView):
    """Удаление всех заказов"""

    def get_object(self):
        try:
            return Orders.objects.all()
        except Orders.DoesNotExist:
            raise Http404

    def delete(self, request, format=None, **kwargs):
        """Метод удаления всех заказов"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetOrdersView(generics.ListAPIView):
    """Вывод заказов"""

    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers.GetOrderSerializer


class FindOrderByIdView(generics.RetrieveAPIView):
    """Поиск заказа по идентификации"""

    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers.GetOrderSerializer
