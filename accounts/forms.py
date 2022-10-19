from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "name":"password1", "id":"form3Example4" ,"class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"type":"email", "name":"password1", "id":"form3Example4" ,"class":"form-control"}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={"type":"text", "name":"password1", "id":"form3Example4" ,"class":"form-control"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={"type":"password", "name":"password1", "id":"form3Example4" ,"class":"form-control"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={"type":"password", "name":"password1", "id":"form3Example4" ,"class":"form-control"}))
    class Meta:
        model = User
        fields = ['username', 'email','phone', 'password1', 'password2']
        
        

        
class profiles(Profile):
    username = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "name":"password1", "id":"form3Example4" ,"class":"form-control"}))
    bio = forms.IntegerField(widget=forms.TextInput(attrs={"type":"text", "name":"password1", "id":"form3Example4" ,"class":"form-control"}))
    
