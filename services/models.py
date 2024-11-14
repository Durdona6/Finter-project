from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=250)

    def __str__(self):
        return self.title