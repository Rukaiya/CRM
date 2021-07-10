from  django.forms import ModelForm, fields
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from  django import  forms

from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class  Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    '''def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['username'].widget.attrs['cols'] = 7
        #self.fields['long_desc'].widget.attrs['rows'] = 20'''