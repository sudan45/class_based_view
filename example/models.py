from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    parentname=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("studentdetail",kwargs={"pk":self.pk})

    def __str__(self):
        return self.name

 
