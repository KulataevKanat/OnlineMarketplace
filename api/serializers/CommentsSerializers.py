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
            'text',
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
            'user_id',
            # 'rate',
            'date',
            'text',
            'product',
        ]
