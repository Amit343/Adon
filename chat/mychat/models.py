from django.db import models

# Create your models here.
class Chat(models.Model):
    room_name=models.CharField(max_length=250)
    allowed_user=models.CharField(max_length=250)