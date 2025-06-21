from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_welcome_email_task

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    """
    Listens for a new user being created and triggers the welcome email task.
    """
    if created:
        send_welcome_email_task.delay(instance.pk) 