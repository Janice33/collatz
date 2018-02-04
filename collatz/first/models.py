from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    no = models.CharField(max_length=100)
    steps= models.CharField(max_length=100, default='null')
    def __str__(self):
        return self.name+'-'+self.no+'-'+self.steps




