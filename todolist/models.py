from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.TextField()
    title = models.TextField()
    description = models.TextField()
    isfinished = models.BooleanField(default=False)

