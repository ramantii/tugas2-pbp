from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class MyWatchList2(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()