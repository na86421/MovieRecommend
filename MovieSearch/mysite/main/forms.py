from django.forms import ModelForm
from main.models import *
from django import *
#from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django.views.generic import CreateView

from django.contrib.auth.forms import UserChangeForm



class CustomUserCreationForm(ModelForm): 
    class Meta:
        model =User
        fields=['username', 'password' , 'email', 'selected1', 'selected2', 'selected3', 'selected4', 'selected5','user_comment','photo']
        username = forms.CharField(
        widget=forms.TextInput(attrs={'class': "col-sm-2 col-form-label"}),
        )
    
class CustomUserChangeForm(UserChangeForm):
    username = None
    password = None
    class Meta:
        model=get_user_model()
        fields=['email', 'user_comment']
        
        
class Form(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email' , 'title', 'comment']
        name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "col-sm-2 col-form-label"}),
        )
"""	
class Signform(ModelForm):
    class Meta:
        model = Signuser
        fields = ['username', 'password' , 'email', 'selected']
        username
		= forms.CharField(
        widget=forms.TextInput(attrs={'class': "col-sm-2 col-form-label"}),
        )
"""