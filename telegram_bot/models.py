from django.db import models

# Create your models here.

class TelegramUser(models.Model):
    chat_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or self.chat_id
