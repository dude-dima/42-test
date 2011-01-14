from django import forms
from models import Customer
from widgets import JQCalendarWidget

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        widgets = {'birth_date': JQCalendarWidget}