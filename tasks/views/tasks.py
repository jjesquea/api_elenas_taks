"""Tasks views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Serializers
from tasks.serializers import TaskModelSerializer

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Model
from tasks.models import Task


class TaskViewSet(viewsets.ModelViewSet):
	"""Task view set."""

	queryset = Task.objects.all()
	serializer_class = TaskModelSerializer
	permission_classes = [IsAuthenticated]

	# Filters & Ordering
	filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
	search_fields = ('title', 'description')
	ordering_fields = ['title']
	filter_fields = ['is_completed']

	def get_queryset(self):
		"""Restrict list to owning user."""

		queryset = Task.objects.all()
		user = self.request.user
		return queryset.filter(user=user)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	@action(detail=True, methods=['patch'])
	def mark_task(self, request, *args, **kwargs):
		"""Change the status of the task depending on the current status."""

		task = self.get_object()
		task.is_completed = not task.is_completed
		task.save()
		serializer = TaskModelSerializer(task)
		return Response(serializer.data)
