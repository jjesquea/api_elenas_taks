"""User models."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utils
from utils.models import ElenasModel


class User(ElenasModel, AbstractUser):
	"""User model.

	Extend from Django's Abstract User, change the username field to email field.
	"""

	email = models.EmailField(
		'email address',
		unique=True,
		error_messages={
			'unique': 'A user with that email already exists.'
		}
	)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	def __str__(self):
		"""Return username."""

		return self.username
