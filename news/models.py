from django.db import models
from django.utils import timezone


class News(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title

