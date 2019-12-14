from django.db import models

# Create your models here.
class Animal(models.Model):
	image = models.ImageField(upload_to='images/')
	Character = models.CharField(max_length=500)
