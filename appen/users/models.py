from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model): 
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=100)
	username = models.CharField(max_length=50)
	mail = models.EmailField()