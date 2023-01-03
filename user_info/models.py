from django.db import models
import uuid


# Create your models here.
class Userinfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    profileImg = models.URLField(max_length=100)
    password = models.CharField(max_length=50)
    chatList = models.CharField(max_length=50)
    addressList = models.CharField(max_length=50)