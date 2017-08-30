from django import forms
from todo.models import ToDo, Category


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['name', 'description', 'date_deadline', 'status', 'time_expected', 'difficulty', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
