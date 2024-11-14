from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    image = models.ImageField(upload_to='about_images/')


    def __str__(self):
        return self.title