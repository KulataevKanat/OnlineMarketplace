from rest_framework import serializers

from api.models import Cart
from api.serializers import ProductSerializers


class CreateCartSerializer(serializers.ModelSerializer):
    """Добавление товара в корзину"""

    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = [
            "id",
            'customer_id',
        ]


class UpdateCartSerializer(serializers.ModelSerializer):
    """Обновление товара из корзины по идентификации"""

    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = [
            "id",
            'customer_id',
        ]


class GetCartSerializer(serializers.ModelSerializer):
    """Вывод товаров из корзины"""

    product_id = ProductSerializers.GetProductSerializer()

    class Meta:
        model = Cart
        fields = [
            'id',
            'product_id',
            'amount',
        ]
