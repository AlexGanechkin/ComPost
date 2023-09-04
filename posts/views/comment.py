

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from posts.models import Comment
from posts.permissions import CommentatorPermission
from posts.serializers.comment import CommentListSerializer, CommentDetailSerializer, CommentCreateSerializer, \
    CommentUpdateSerializer, CommentDestroySerializer


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]


class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [AllowAny]


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [CommentatorPermission]


class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDestroySerializer
    permission_classes = [CommentatorPermission]
