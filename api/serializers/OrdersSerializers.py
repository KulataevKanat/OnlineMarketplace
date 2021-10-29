from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from api import service
from api.models import Orders
from api.serializers import ProductHistorySerializers


class CreateOrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Добавление заказа"""

    product_history = ProductHistorySerializers.CreateProductHistorySerializer(many=True, allow_null=True,
                                                                               source='orders')
    status = service.ChoiceField(choices=Orders.PRODUCT_STATUS)

    class Meta:
        model = Orders
        fields = [
            'id',
            'client_id',
            'product_history',
            # 'address',
            # 'phone',
            'date',
            'status',

        ]
        read_only_fields = [
            'id',
            'client_id',
            'product_history',
            'date',
            'status',
        ]


class UpdateOrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    """Обновление заказа по идентификации"""

    product_history = ProductHistorySerializers.UpdateProductHistorySerializer(many=True, allow_null=True,
                                                                               source='orders')
    status = service.ChoiceField(choices=Orders.PRODUCT_STATUS)

    class Meta:
        model = Orders
        fields = [
            'id',
            'client_id',
            'product_history',
            # 'address',
            # 'phone',
            'date',
            'status',

        ]
        read_only_fields = [
            'id',
            'client_id',
            'product_history',
            'date',
            'status',
        ]


class GetOrderSerializer(serializers.ModelSerializer):
    """Вывод заказов"""

    product_history = ProductHistorySerializers.GetProductHistorySerializer(many=True, source='orders')
    status = service.ChoiceField(choices=Orders.PRODUCT_STATUS)

    class Meta:
        model = Orders
        fields = [
            'id',
            'client_id',
            'product_history',
            # 'address',
            # 'phone',
            'date',
            'status',

        ]
