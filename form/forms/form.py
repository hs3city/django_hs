from django import forms



class UserForm(forms.Form):
    name = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(max_length=70,widget=forms.PasswordInput, label="Password")