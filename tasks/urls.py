"""Tasks URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from tasks import views as task_views

router = DefaultRouter()
router.register(r'tasks', task_views.TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls))
]
