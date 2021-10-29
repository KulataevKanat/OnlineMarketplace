from rest_framework import serializers

from api.models import ProductHistory


class CreateProductHistorySerializer(serializers.ModelSerializer):
    """Добавление истории товара"""

    class Meta:
        model = ProductHistory
        fields = [
            'id',
            'prod_id',
            'title',
            'description',
            'creation_date',
            'price',
            'amount',

        ]
        read_only_fields = [
            'id'
            'creation_date'
        ]


class UpdateProductHistorySerializer(serializers.ModelSerializer):
    """Обновление истории товара по идентификации"""

    class Meta:
        model = ProductHistory
        fields = [
            'id',
            'prod_id',
            'title',
            'description',
            'creation_date',
            'price',
            'amount',

        ]
        read_only_fields = [
            'id'
            'creation_date'
        ]


class GetProductHistorySerializer(serializers.ModelSerializer):
    """Вывод истории товаров"""

    class Meta:
        model = ProductHistory
        fields = [
            'id',
            'prod_id',
            'title',
            'description',
            'creation_date',
            'price',
            'amount',

        ]
