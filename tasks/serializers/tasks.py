"""Task Serializers."""

# Django REST Framework
from rest_framework import serializers

# Tasks
from tasks.models import Task


class TaskModelSerializer(serializers.ModelSerializer):
	"""Task serializer."""

	class Meta:
		"""Meta class."""

		model = Task
		fields = (
			'title',
			'description',
			'is_completed',
			'created_at',
			'modified_at'
		)
		read_only_fields = (
			'is_completed',
			'created_at',
			'modified_at'
		)
