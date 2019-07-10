from django.db import models

# Create your models here.

class Client(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
   
    
    def __str__(self):
        return self.fname
      

class Subscribe(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email