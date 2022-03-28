"""Task models Admin."""

# Django
from django.contrib import admin

# Tasks
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	"""Task model admin."""

	list_display = ("title", "description", "created_at", "user")
	list_filter = ("title", "description")
	search_fields = ("title", "description", "user__username", "user__email", "user__first_name", "user__last_name")
