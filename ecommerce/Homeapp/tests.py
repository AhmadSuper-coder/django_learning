from django.test import TestCase

# Create your tests here.

from celery import shared_task


@shared_task
def add(x, y):
    return x + y