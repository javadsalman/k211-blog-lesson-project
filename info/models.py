from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name