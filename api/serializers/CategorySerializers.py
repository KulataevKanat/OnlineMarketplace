from rest_framework import serializers

from api.models import Category


class CreateCategorySerializer(serializers.ModelSerializer):
    """Добавление категории"""

    class Meta:
        model = Category
        fields = '__all__'


class UpdateCategorySerializer(serializers.ModelSerializer):
    """Обновление категории по идентификации"""

    class Meta:
        model = Category
        fields = '__all__'


class GetCategorySerializer(serializers.ModelSerializer):
    """Вывод категорий"""

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]
