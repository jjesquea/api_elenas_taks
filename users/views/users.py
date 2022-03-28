"""Users views."""

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from users.serializers import (
	UserLoginSerializer, UserModelSerializer, UserSignUpSerializer
)

# Models
from users.models import User


class UserLoginAPIView(viewsets.GenericViewSet):
	"""User Login APIView."""

	queryset = User.objects.filter(is_active=True)
	serializer_class = UserModelSerializer

	@action(detail=False, methods=['post'])
	def login(self, request):
		"""Handle HTTP POST to user sign in."""
		serializer = UserLoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user, token = serializer.save()
		data = {
			'user': UserModelSerializer(user).data,
			'access_token': token
		}
		return Response(data, status=status.HTTP_201_CREATED)

	@action(detail=False, methods=['post'])
	def signup(self, request):
		"""Handle HTTP POST to create user."""
		serializer = UserSignUpSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		data = UserModelSerializer(user).data
		return Response(data, status=status.HTTP_201_CREATED)
