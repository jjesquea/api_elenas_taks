"""Factory to create users and tasks."""

import os
import time
import django
from random import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elenasTasks.settings")

django.setup()

# Models
from users.models import User
from tasks.models import Task


def generate_number():
	return int(random()*10+1)


def generate_users(count):
	"""Generate a specific number of users."""

	for u in range(count):
		first_name_random = 'Test{}'.format(generate_number())
		last_name_random = 'Test{}'.format(generate_number())
		email_random = 'test{}@test.com'.format(u + 1)
		username_random = 'test{}'.format(generate_number())
		password_random = 'Admin123$'

		User.objects.create(
			first_name=first_name_random,
			last_name=last_name_random,
			email=email_random,
			username=username_random,
			password=password_random
		)


def generate_tasks():
	users = User.objects.all()
	number_tasks = users.count() * 10
	for user in users:
		for t in range(number_tasks):
			title_random = 'Title test{}'.format(generate_number())
			description_random = 'Description test{}'.format(generate_number())

			Task.objects.create(
				title=title_random,
				description=description_random,
				user=user
			)


if __name__ == "__main__":
	print('Loading data')
	print('Please wait...')
	start = time.strftime('%c')
	print(f'Init at: {start}')
	generate_users(2)
	generate_tasks()
	end = time.strftime('%c')
	print(f'Completed at: {end}')

