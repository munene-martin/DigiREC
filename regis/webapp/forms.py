from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class register(UserCreationForm):
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    

    class Meta:
        model= User
        fields=('username','first_name','last_name','email','password1','password2')

        def __init__(self):
            super(register,self).__init__()
            self.fields['username'].widget.attrs['class']='form-control'
            self.fields['first_name'].widget.attrs['class']='form-control'
            self.fields['last_name'].widget.attrs['class']='form-control'
            self.fields['email'].widget.attrs['class']='form-control'
            self.fields['password1'].widget.attrs['class']='form-control'
            self.fields['password2'].widget.attrs['class']='form-control'
