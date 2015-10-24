from rest_framework import serializers
from django.contrib.auth import authenticate, login
from accounts import models


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is inactive!")
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError("Invalid credentials!")
        else:
            raise serializers.ValidationError("Missing fields!")

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'email',
            'auth_token',
        )
        write_only_fields = (
            'password',
        )
        read_only_fields = (
            'auth_token',
        )

    def create(self, attrs, instance=None):
        user = models.User.objects.create_user(**attrs)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'email',
        )
