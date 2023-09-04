
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from users.models import User
from users.permissions import UserPermission
from users.serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer, UserUpdateSerializer, \
    UserDestroySerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [UserPermission]


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
    permission_classes = [IsAdminUser]
