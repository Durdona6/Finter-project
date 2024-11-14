from django.db import models

class Home(models.Model):
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email

class Index(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=150)


    def __str__(self):
        return self.title