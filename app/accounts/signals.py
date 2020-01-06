from notifications.signals import notify

from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in

from .models import Account, Profile

def create_profile_handler(sender, instance, created, **kwargs):
    try:
        profile = instance.profile
    except Profile.DoesNotExists:
        Profile.objects.create(account=instance)


def register_handlers():
    pass
    # user_logged_in.connect(create_profile_handler)
    # # post_save.connect(
    # #     create_profile_handler,
    # #     sender=Account,     
    # # )