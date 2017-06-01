from django.shortcuts import render
from django.middleware import csrf
from django.template import Template, Context


# Create your views here.
# def simple_templa(request):
#     csrf_token = csrf.get_token(request)
#     our_template = Template("""
#                <form method='POST'>
#                <textarea name='hacking'></textarea>
#                <input type ='hidden' name='csrf_token' value='{% csrf_token %}'>
#                <input type='submit' value='SEND'>
#                """)
#     our_context = Context({})
#
#     return our_template.render(our_context)

def simple_templa(request):
    our_variable = 'hey'
    our_integer = 12
    our_form = """
        <br/>
        <div>
        <textarea name='hacking'></textarea>
        <input type='submit' value='SEND'>
        </div>
    """
    return render(request, 'simple_template.html', {'our_variable': our_variable,
                                                    'our_integer': our_integer,
                                                    'our_form': our_form})
