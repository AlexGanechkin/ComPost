from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from posts.models import Post
from posts.permissions import AuthorPermission
from posts.serializers.post import PostListSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateSerializer, \
    PostDestroySerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [AuthorPermission]


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDestroySerializer
    permission_classes = [AuthorPermission]
