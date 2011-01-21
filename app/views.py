from django.shortcuts import render_to_response
from models import Customer


def contact_view(request):
    """Shows default contact information"""
    try:
        customer = Customer.objects.get(name="Dmitry")
    except:
        customer = Customer()
        customer.name = "Dmitry"
        customer.surname = "Razumov"
        customer.bio = "Some bio"
        customer.contacts = "380500000000"
        customer.save()
    return render_to_response('contacts.html', {'user': customer})
