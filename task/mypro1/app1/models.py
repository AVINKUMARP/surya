from django.db import models
class student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=25)
    place=models.CharField(max_length=20)


# Create your models here.
