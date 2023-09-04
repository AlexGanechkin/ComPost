from rest_framework import serializers

from posts.models import Comment
from users.models import User


class CommentListSerializer(serializers.ModelSerializer):
    commentator = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'text', 'commentator']


class CommentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    commentator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # commentator = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'text', 'commentator', 'post']


class CommentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['text']


class CommentDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id']
