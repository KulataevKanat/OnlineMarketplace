from rest_framework import generics

from api.models import Category
from api.serializers import CategorySerializers


class CreateCategoryView(generics.CreateAPIView):
    """Добавление категории"""

    serializer_class = CategorySerializers.CreateCategorySerializer


class DeleteCategoryByIdView(generics.DestroyAPIView):
    """Удаление категории по идентификации"""

    queryset = Category.objects.all()


class UpdateCategoryByIdView(generics.UpdateAPIView):
    """Обновление категории по идентификации"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializers.UpdateCategorySerializer


class GetCategoryView(generics.ListAPIView):
    """Вывод категорий"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializers.GetCategorySerializer


class FindCategoryByIdView(generics.RetrieveAPIView):
    """Поиск категории по идентификации"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializers.GetCategorySerializer
