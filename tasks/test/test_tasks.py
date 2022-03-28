"""Users test."""

# Django
import json

from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Model
from users.models import User
from tasks.models import Task


class TaskAPITestCase(APITestCase):
	"""User API test case."""

	def setUp(self) -> None:
		"""Test case setup"""

		self.user = User.objects.create(
			first_name='Test name',
			last_name='Test lastname',
			email='test@test.com',
			username='test',
			password='test$123'
		)
		self.user_two = User.objects.create(
			first_name='Test',
			last_name='Test',
			email='test2@test.com',
			username='test2',
			password='test$1233'
		)

	def authenticate(self, user):
		self.token = Token.objects.create(user=user).key
		self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))

	def test_should_not_create_task(self):
		"""Not should create task."""
		simple_data = {
			'title': 'Test title',
			'description': 'Test description'
		}
		response = self.client.post(reverse('tasks:tasks-list'), simple_data)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_should_create_task(self):
		"""Should create task with user credentials."""
		simple_data = {
			'title': 'Test 2 title',
			'description': 'Test description'
		}
		self.authenticate(self.user)
		response = self.client.post(reverse('tasks:tasks-list'), simple_data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data['title'], simple_data['title'])
		self.assertEqual(response.data['description'], simple_data['description'])
		self.assertEqual(response.data['is_completed'], False)

	def test_should_not_create_task_because_description_empty(self):
		"""Not Should create task because description empty."""
		simple_data = {
			'title': 'Test 2 title',
			'description': ''
		}
		self.authenticate(self.user)
		response = self.client.post(reverse('tasks:tasks-list'), simple_data)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_should_list_tasks_by_user(self):
		"""Should list tasks by user."""
		Task.objects.create(title='Test task', description='Test task description', user=self.user_two)
		simple_data = {
			'title': 'Test 3 title',
			'description': 'Test 3 description'
		}
		self.authenticate(self.user)
		response = self.client.post(reverse('tasks:tasks-list'), simple_data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Task.objects.filter(user=self.user).count(), 1)
		self.assertEqual(Task.objects.all().count(), 2)

		resp = self.client.get(reverse('tasks:tasks-list'))
		self.assertIsInstance(resp.data['results'], list)

	def test_should_mark_tasks_as_uncompleted(self):
		"""Should mark tasks as uncompleted."""
		task = Task.objects.create(title='Test task', description='Test task description', user=self.user_two, is_completed=True)
		self.authenticate(self.user_two)
		response = self.client.patch(reverse('tasks:tasks-mark-task', kwargs={'pk': task.pk}))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['is_completed'], False)

	def test_should_mark_tasks_as_completed(self):
		"""Should mark tasks as completed."""
		task = Task.objects.create(title='Test task', description='Test task description', user=self.user_two)
		self.authenticate(self.user_two)
		response = self.client.patch(reverse('tasks:tasks-mark-task', kwargs={'pk': task.pk}))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['is_completed'], True)

	def test_should_update_data_tasks(self):
		"""Should update data tasks."""
		task = Task.objects.create(title='Test task', description='Test task description', user=self.user)
		simple_data = {
			'title': 'Test 3 title',
			'description': 'Test 3 description'
		}
		self.authenticate(self.user)
		response = self.client.put(reverse('tasks:tasks-detail', kwargs={'pk': task.pk}), data=simple_data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['title'], simple_data['title'])
		self.assertEqual(response.data['description'], simple_data['description'])

	def test_should_delete_tasks(self):
		"""Should delete task."""
		task = Task.objects.create(title='Test task', description='Test task description', user=self.user_two, is_completed=True)
		self.authenticate(self.user_two)
		response = self.client.delete(reverse('tasks:tasks-detail', kwargs={'pk': task.pk}))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(Task.objects.count(), 0)
