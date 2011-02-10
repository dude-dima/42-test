from django import forms
from app.models import Customer
from app.widgets import JQCalendarWidget


class CustomerForm(forms.ModelForm):

    def __init__(self, *args, **kw):
        super(forms.ModelForm, self).__init__(*args, **kw)
        self.fields.keyOrder.reverse()

    class Meta:
        model = Customer
        widgets = {'birth_date': JQCalendarWidget}
