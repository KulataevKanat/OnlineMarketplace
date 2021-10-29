from rest_framework import generics

from api.models import Comments
from api.serializers import CommentsSerializers


class CreateCommentView(generics.CreateAPIView):
    """Добавление комментарии"""

    serializer_class = CommentsSerializers.CreateCommentSerializer


class CreateRelpliesView(generics.CreateAPIView):
    """Добавление ответа к коментарии"""

    serializer_class = CommentsSerializers.CreateRelpliesSerializer


class DeleteCommentByIdView(generics.DestroyAPIView):
    """Удаление комментарии по идентификации"""

    queryset = Comments.objects.all()


class UpdateCommentByIdView(generics.UpdateAPIView):
    """Обновление комментарии по идентификации"""

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers.UpdateCommentSerializer


class GetCommentView(generics.ListAPIView):
    """Вывод комментарий"""

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers.GetCommentSerializer


class FindCommentByIdView(generics.RetrieveAPIView):
    """Поиск комментарии по идентификации"""

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers.GetCommentSerializer
