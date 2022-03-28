"""User models Admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Users
from users.models import User


class CustomUserAdmin(UserAdmin):
	"""User model admin."""

	list_display = ("email", "username", "first_name", "last_name")
	list_filter = ("created_at", "modified_at")


admin.site.register(User, CustomUserAdmin)

