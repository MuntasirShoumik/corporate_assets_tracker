from django import forms
from django.forms import PasswordInput
from .models import Company,Employee,Device,DeviceLog
from django.core.validators import *
import re
from datetime import datetime

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= Company
        fields = "__all__"



    def pass_check(val):
        if not bool(re.search(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', val)):
            raise forms.ValidationError("minimum 8 characters in length, At least one uppercase English letter, At least one lowercase English letter, At least one digit, At least one special character!")
         

    name = forms.CharField(max_length=50,label="First name")
    address = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(label="Email",required=True)
    password = forms.CharField(widget=forms.PasswordInput,validators=[pass_check],label="Password",required=True)  



class LoginForm(forms.Form):
    company_name = forms.CharField()
    password = forms.CharField(widget=PasswordInput())


class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields = "__all__"



class CreateDeviceForm(forms.ModelForm):
    class Meta:
        model= Device
        fields = "__all__"


class AllocateDeviceForm(forms.ModelForm):
    class Meta:
        model= DeviceLog
        exclude = ('check_in','in_condition')

    check_out = forms.DateTimeField(initial=datetime.now())

class DeallocateDeviceForm(forms.ModelForm):
    class Meta:
        model= DeviceLog
        fields = "__all__"

    check_in = forms.DateTimeField(initial=datetime.now())

class SearchDeviceForm(forms.Form):
    sn = forms.IntegerField()          