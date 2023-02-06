from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=123)
    position = models.CharField(max_length=123)
    date_employment = models.DateField()
    salary = models.FloatField()
    image = models.ImageField(upload_to='images')






