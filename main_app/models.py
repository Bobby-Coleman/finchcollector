from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'pk':self.id})
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
