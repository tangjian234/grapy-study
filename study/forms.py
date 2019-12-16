#=====================**************=========: Form input
from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

class VehicleForm(forms.Form):
    make = forms.CharField()
    model = forms.CharField()
    year = forms.IntegerField()

class VehicleView(FormView):
    form_class = VehicleForm
    template_name = 'input.html'
    success_url = reverse_lazy('success')    

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class PersonalDataForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=255)
    last_name = forms.CharField(required=True, max_length=255)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=200)
    address = forms.CharField(max_length=1000, widget=forms.Textarea())