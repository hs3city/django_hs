from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'kategoria'
        verbose_name_plural = 'kategorie'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('todo:categoryformadd')

class ToDo(models.Model):
    TODO = 'TD'
    DONE = 'DN'
    STATUS = (
        (TODO, 'Aktywny'),
        (DONE, 'Wykonane')
    )
    DIFFICULTY = (
        (1, 'Od ręki'),
        (3, 'Prosty'),
        (5, 'Średnie'),
        (8, 'Trudne'),
        (13, 'Bardzo trudne'),
    )

    name = models.CharField(max_length=250)
    description = models.TextField(verbose_name='Opis')
    date_created = models.DateField(auto_now_add=True)
    date_deadline = models.DateField(default=None)
    status = models.CharField(max_length=2, choices=STATUS)
    active = models.BooleanField(default=True)
    time_expected = models.IntegerField(default=15)
    difficulty = models.IntegerField(choices=DIFFICULTY)
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = 'zadanie'
        verbose_name_plural = 'zadania'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('todo:todoformadd')
