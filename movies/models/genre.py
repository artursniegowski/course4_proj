from django.db import models


class Genre(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.TextField(unique=True)
