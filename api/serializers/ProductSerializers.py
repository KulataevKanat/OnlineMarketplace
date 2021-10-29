from rest_framework import serializers

from api.models import Product
from api.serializers.CategorySerializers import GetCategorySerializer


class CreateProductSerializer(serializers.ModelSerializer):
    """Добавление товара"""

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'creation_date',
            'price',
            'supplier',
            'product_category',

        ]


class UpdateProductSerializer(serializers.ModelSerializer):
    """Обновление товара"""

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'creation_date',
            'price',
            'supplier',
            'product_category',

        ]


class GetProductSerializer(serializers.ModelSerializer):
    """Вывод и Поиск товаров"""

    product_category = GetCategorySerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'creation_date',
            'price',
            'supplier',
            'product_category',

        ]
