from django.db import models


# Create your models here.

class ShoppingItem(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    job = models.ForeignKey('Job')


class Job(models.Model):
    jobtitle = models.CharField(max_length=50)


class Department(models.Model):
    name = models.CharField(max_length=120)


class Section(models.Model):
    name = models.CharField(max_length=120)
    department = models.ForeignKey('Department')
