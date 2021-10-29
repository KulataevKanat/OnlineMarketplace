from rest_framework import serializers

from api.models import User


class GetUserSerializer(serializers.ModelSerializer):
    """Вывод и Поиск пользователей"""

    groups = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'groups',
            'is_supplier',
        ]


class AuthSerializer(serializers.ModelSerializer):
    """Авторизация, вывод access и refresh токена"""

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    """Регистрация пользователя"""

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'groups',
            'is_supplier',
        ]
        read_only_fields = [
            'id',
            'is_supplier',
        ]


class CreateSuperUserSerializer(serializers.ModelSerializer):
    """Добавление супер пользователя"""

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'groups',
        ]

    def create(self, validated_data):
        superuser = User.objects._create_superuser(username=validated_data.__getitem__('username'),
                                                   groups=validated_data.__getitem__('groups'),
                                                   email=validated_data.__getitem__('email'),
                                                   password=validated_data.__getitem__('password'),
                                                   )

        return superuser


class UpdateUserSerializer(serializers.ModelSerializer):
    """Изменение пользователя по идентификации"""

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'is_supplier',
        ]
