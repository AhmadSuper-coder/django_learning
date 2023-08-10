from celery import shared_task


@shared_task
def add_two_number(x, y):
	return x + y



