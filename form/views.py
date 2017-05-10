from django.shortcuts import render
from .forms.form import UserForm
from .models import User

# Create your views here.
def post_form(request):
    if(request.method == 'POST'):
        form = UserForm(request.POST)
        if(form.is_valid()):
            return render(request, "simple_response.html",
                          {'username' : form.cleaned_data['name'],
                           'password' : form.cleaned_data['password']})

    elif(request.method == 'GET'):
        form = UserForm(request.POST)
        return render(request, "form_template.html", {'our_form': form})
