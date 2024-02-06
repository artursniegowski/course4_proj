from django.db import models


class SearchTerm(models.Model):
    class Meta:
        ordering = ["id"]

    term = models.TextField(unique=True)
    last_search = models.DateTimeField(auto_now=True)
