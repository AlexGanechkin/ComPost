
from rest_framework import serializers

from users.models import User
from users.validators import validate_password_format, validate_email_format


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'is_staff']


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    password = serializers.CharField(max_length=50, validators=[validate_password_format])
    email = serializers.CharField(max_length=100, validators=[validate_email_format])

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'phone_number', 'birth_day', 'email']

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100, validators=[validate_email_format])

    class Meta:
        model = User
        fields = ['username', 'password', 'phone_number', 'birth_day', 'email']


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
