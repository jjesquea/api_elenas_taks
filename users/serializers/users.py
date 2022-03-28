"""User serializers."""

# Django
from django.contrib.auth import password_validation, authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """User Model Serializer."""

    class Meta:
        """Meta Class."""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


class UserLoginSerializer(serializers.Serializer):
    """User Login Serializer."""

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=128)

    def validate(self, data):
        """Validate user authentication."""

        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials.')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve token."""

        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserSignUpSerializer(serializers.Serializer):
    """User SignUp Serializer."""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, max_length=128)
    password_confirmation = serializers.CharField(min_length=8, max_length=128)
    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)

    def validate(self, data):
        """Validate user creation."""

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match.')
        password_validation.validate_password(password)
        return data

    def create(self, data):
        """Create user."""

        data.pop('password_confirmation')
        return User.objects.create(**data)
