
from rest_framework import serializers, request

from posts.models import Post
from posts.validators import ForbiddenWordsValidator, BirthDayValidator
from users.models import User


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'author']


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        validators=[BirthDayValidator()])
    title = serializers.CharField(max_length=100, validators=[ForbiddenWordsValidator()])

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'author']


class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'text', 'author']


class PostDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id']

