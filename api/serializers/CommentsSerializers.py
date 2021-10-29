from rest_framework import serializers

from api.models import Comments


class CreateCommentSerializer(serializers.ModelSerializer):
    """Добавление комментарии"""

    class Meta:
        model = Comments
        exclude = [
            'relplies',
        ]
        read_only_fields = [
            "id",
            'user_id',
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
        read_only_fields = [
            "id",
            'user_id',
        ]


class GetCommentSerializer(serializers.ModelSerializer):
    """Вывод комментарий"""

    user_id = serializers.StringRelatedField()

    class Meta:
        model = Comments
        fields = [
            'id',
            'user_id',
            # 'rate',
            'date',
            'text',
            'product',
            'relplies',
        ]
        depth = 10

