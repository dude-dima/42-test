from django.template import Template, Context
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import User

def contact_view(request):
    #u = User()
    #u.name = "Dmitry"
    #u.surname = "Razumov"
    #u.bio = "Some bio"
    #u.contacts = "380500000000"
    #u.save()
    try:
        u = User.objects.get(name = "Dmitry")
    except:
        u = None
    return render_to_response('contacts.html', {'user':u})