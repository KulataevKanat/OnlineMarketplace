from rest_framework import generics

from api.models import Comments
from api.serializers import CommentsSerializers


class CreateCommentView(generics.CreateAPIView):
    """Добавление комментарии"""

    serializer_class = CommentsSerializers.CreateCommentSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class CreateRelpliesView(generics.CreateAPIView):
    """Добавление ответа к коментарии"""

    serializer_class = CommentsSerializers.CreateRelpliesSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class DeleteCommentByIdView(generics.DestroyAPIView):
    """Удаление комментарии по идентификации"""

    queryset = Comments.objects.all()


class UpdateCommentByIdView(generics.UpdateAPIView):
    """Обновление комментарии по идентификации"""

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers.UpdateCommentSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class GetCommentView(generics.ListAPIView):
    """Вывод комментарий"""

    queryset = Comments.objects.filter(relplies= not None)
    serializer_class = CommentsSerializers.GetCommentSerializer


class FindCommentByIdView(generics.RetrieveAPIView):
    """Поиск комментарии по идентификации"""

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers.GetCommentSerializer
