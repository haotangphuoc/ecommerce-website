from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput
from django import forms 
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re enter password'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


    
        