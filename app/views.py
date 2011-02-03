from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from models import Customer, Request
from forms import CustomerForm
import tools


def contact_view(request):
    c = tools.get_default_context(request, 'm_contacts')
    c['customer'] = Customer.objects.all()[0]
    return render_to_response('contacts.html', c,
                              context_instance=RequestContext(request))


def request_view(request):
    c = tools.get_default_context(request, 'm_requests')
    try:
        c['requests'] = Request.objects.all()[:10]
    except:
        pass
    return render_to_response('requests.html', c,
                              context_instance=RequestContext(request))


@login_required
def edit_view(request):
    c = tools.get_default_context(request, 'm_edit')
    if request.method == 'POST':  # If the form has been submitted...
        form = CustomerForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            customer = Customer.objects.all()[0]
            customer.name = form.cleaned_data['name']
            customer.surname = form.cleaned_data['surname']
            customer.bio = form.cleaned_data['bio']
            customer.contacts = form.cleaned_data['contacts']
            customer.birth_date = form.cleaned_data['birth_date']
            customer.save()
            # Is that Ajax?
            if request.is_ajax():
                return HttpResponse("Data stored successfuly!")
            return HttpResponseRedirect('/')  # Redirect after POST
    else:
        customer = Customer.objects.all()[0]
        form = CustomerForm(instance=customer)  # An unbound form

    c['form'] = form
    return render_to_response('edit.html', c,
                              context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return contact_view(request)
