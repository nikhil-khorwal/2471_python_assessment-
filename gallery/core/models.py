from django.db import models
from django.contrib.auth.models import User

class Gallary(models.Model):
  image_name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='images')
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)