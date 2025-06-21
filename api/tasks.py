from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def send_welcome_email_task(user_id):
    """
    Sends a welcome email to the user after registration.
    """
    try:
        user = User.objects.get(pk=user_id)
        subject = 'Welcome to Our Awesome Site!'
        message = f'Hi {user.username},\n\nThank you for registering. We are happy to have you!'
        from_email = 'noreply@example.com'  # This can be configured in settings.py
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)
        return f"Welcome email sent to {user.email}"
    except User.DoesNotExist:
        return f"User with id {user_id} does not exist." 