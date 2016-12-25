from django.db import models
from django.utils import timezone


class Post(models.Model):
    keyword = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.keyword
