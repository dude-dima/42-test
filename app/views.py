from django.template import Template, Context
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import User, Request

def contact_view(request):
    ### Just for storing data into database
    #u = User()
    #u.name = "Dmitry"
    #u.surname = "Razumov"
    #u.bio = "Some bio"
    #u.contacts = "380500000000"
    #u.save()
    try:
        u = User.objects.get(pk=1)
    except:
        u = None
    return render_to_response('contacts.html', {'user':u})

def request_view(request):
    try:
        r = Request.objects.all()[:10]
    except:
        r = None
    return render_to_response('requests.html', {'requests':r})