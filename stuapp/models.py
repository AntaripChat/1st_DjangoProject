from django.db import models

# Create your models here.
class studentdata(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    roll = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return (self.name)
