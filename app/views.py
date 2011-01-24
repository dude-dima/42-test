from django.shortcuts import render_to_response
from models import Customer


def contact_view(request):
    """Shows default contact information"""
    customer = Customer.objects.get(name="Dmitry")
    return render_to_response('contacts.html', {'customer': customer})
