from django.template import Template, Context, RequestContext
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Customer, Request

def contact_view(request):
    try:
        u = Customer.objects.get(pk=1)
    except:
        ### Just for storing data into database
        u = Customer()
        u.name = "Dmitry"
        u.surname = "Razumov"
        u.bio = "Some bio"
        u.contacts = "380500000000"
        u.save()

    return render_to_response('contacts.html', {'user':u}, \
                              context_instance=RequestContext(request))

def request_view(request):
    try:
        r = Request.objects.all()[:10]
    except:
        r = None
    return render_to_response('requests.html', {'requests':r})