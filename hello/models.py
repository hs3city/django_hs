from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField()
    job = models.ForeignKey('Job')
    section = models.ForeignKey('Section')

    class Meta:
        verbose_name = "użytkownik"
        verbose_name_plural = "użytkownicy"

    def __str__(self):
        return self.name


class Job(models.Model):
    jobtitle = models.CharField(max_length=50)

    def __str__(self):
        return self.jobtitle


class Department(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = "wydział"
        verbose_name_plural = "wydziały"

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=120)
    department = models.ForeignKey('Department')

    class Meta:
        verbose_name = "pracownia"
        verbose_name_plural = "pracownie"

    def __str__(self):
        return self.name
