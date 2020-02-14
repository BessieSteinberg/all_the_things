from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['display_name', 'username', 'email', 'password']

    def create(self, validated_data):
        # TODO: error if not all fields are filled
        # TODO: error if username is already in use
        user = User.objects.create_user(
            display_name=validated_data['display_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user
