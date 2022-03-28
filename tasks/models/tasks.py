"""User models."""

# Django
from django.db import models
from users.models import User

# Utils
from utils.models import ElenasModel


class Task(ElenasModel):
	"""Task model.

	Record each of the tasks created by users.
	"""
	title = models.CharField(
		'title task',
		max_length=100,
		help_text='Title for which task was created.'
	)
	description = models.TextField(
		'description task',
		help_text='Description for which task was created.'
	)
	is_completed = models.BooleanField(default=False)
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='tasks'
	)

	def __str__(self):
		"""Return task title."""

		return self.title
