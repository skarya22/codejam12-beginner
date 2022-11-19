from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    length = models.IntegerField()

    pub_date = models.DateField(blank=True, default=timezone.now)
    cover = models.FileField(upload_to='covers/', blank=True, default=None, null=True)

    def __str__(self) -> str:
        return self.name
