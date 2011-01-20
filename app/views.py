from django.template import Template, Context
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Customer

def contact_view(request):    
    try:
        u = Customer.objects.get(name="Dmitry")
    except:
        u = Customer()
        u.name = "Dmitry"
        u.surname = "Razumov"
        u.bio = "Some bio"
        u.contacts = "380500000000"
        u.save()
    return render_to_response('contacts.html', {'user': u})
