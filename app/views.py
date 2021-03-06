from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from app.models import Customer, Request
from app.forms import CustomerForm
from app import listeners
from app import tools


def contact_view(request):
    c = tools.get_default_context(request, 'm_contacts')
    c['customer'] = Customer.objects.all()[0]
    return render_to_response('contacts.html', c,
                              context_instance=RequestContext(request))


def request_view(request):
    if request.is_ajax():
        id = request.POST.get("id", 0)
        if id:
            req = Request.objects.get(id=int(id))
            req.priority += 1
            req.save()
            return HttpResponse(id + ";" + str(req.priority))
    c = tools.get_default_context(request, 'm_requests')
    if int(request.POST.get('priority', 0)):
        c['high'] = True
        c['requests'] = Request.objects.order_by('-priority')[:10]
    else:
        c['requests'] = Request.objects.order_by('priority')[:10]
    return render_to_response('requests.html', c,
                              context_instance=RequestContext(request))


@login_required
def edit_view(request):
    c = tools.get_default_context(request, 'm_edit')
    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data and instance
        form = CustomerForm(request.POST, instance=Customer.objects.all()[0])
        if form.is_valid():
            form.save()  # Saving form to model
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


def tag_view(request):
    c = tools.get_default_context(request, 'm_tag')
    return render_to_response('tag.html', c,
                               context_instance=RequestContext(request))
