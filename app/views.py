from django.shortcuts import render_to_response
from models import Customer, Request


def contact_view(request):
    """Shows default contact information"""
    customer = Customer.objects.get(name="Dmitry")
    return render_to_response('contacts.html', {'customer': customer})


def request_view(request):
    try:
        requests = Request.objects.all()[:10]
    except:
        requests = None
    return render_to_response('requests.html', {'requests': requests})
