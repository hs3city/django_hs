from django import forms
# from hello.models import Job


class JobForm (forms.Form):
    jobtitle = forms.CharField()
