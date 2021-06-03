from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    username = forms.CharField(label=("Username"),max_length=100) #,placeholder = 'Enter username') 
	#, widgets=forms.textinput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password')