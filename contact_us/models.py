from django.db import models

class Contact(models.Model):
    class PersonSelect(models.TextChoices):
        ONE = 'Service 1',
        TWO = 'Service 2',
        THREE = 'Service 3'
    
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    select_service = models.CharField(choices=PersonSelect.choices, default=PersonSelect.ONE, max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name
