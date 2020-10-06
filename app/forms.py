from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import MyUser  

class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password','first_name','last_name','phone_number')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','type':'password'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control'}),
        }