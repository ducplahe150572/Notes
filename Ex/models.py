from django.db import models


class Notes(models.Model):
    name = models.CharField(max_length=150)
