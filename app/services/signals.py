from django.db.models.signals import post_save
from notifications.signals import notify
from .models import JobChangeRequest

def my_handler(sender, instance, created, **kwargs):
    notify.send(instance, verb='was created')


def register():
    post_save.connect(
        my_handler,
        sender=JobChangeRequest
    )