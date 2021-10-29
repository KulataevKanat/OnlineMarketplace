from rest_framework import serializers

from api.models import Comments


class CreateCommentSerializer(serializers.ModelSerializer):
    """Добавление комментарии"""

    class Meta:
        model = Comments
        exclude = [
            'relplies',
        ]


class CreateRelpliesSerializer(serializers.ModelSerializer):
    """Добавление ответа к комментарии"""

    class Meta:
        model = Comments
        fields = [
            'relplies',
            'name',
        ]


class UpdateCommentSerializer(serializers.ModelSerializer):
    """Обновление комментарии по идентификации"""

    class Meta:
        model = Comments
        fields = '__all__'


class GetCommentSerializer(serializers.ModelSerializer):
    """Вывод комментарий"""

    class Meta:
        model = Comments
        fields = [
            'id',
            'name',
        ]
