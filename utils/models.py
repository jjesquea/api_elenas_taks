"""Django models utilities."""

# Django
from django.db import models


class ElenasModel(models.Model):
	"""Elenas base model.

	ElenasModel acts as an abstract base class from which every
	other model in the project will inherit. This class provides
	the following attributes:
		- created_at (DateTime): the datetime the object was created
		- modified_at (DateTime): the last datetime the object was modified
	"""

	created_at = models.DateTimeField(
		auto_now_add=True,
		help_text='Date time for which object was created.'
	)
	modified_at = models.DateTimeField(
		auto_now=True,
		help_text='Date time for which object was last modified.'
	)

	class Meta:
		"""Meta options."""

		abstract = True

		get_latest_by = 'created_at'
		ordering = ['-created_at', 'modified_at']
