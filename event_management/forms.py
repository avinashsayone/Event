from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Event, User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    age = forms.IntegerField()
    address=forms.CharField(widget=forms.Textarea)
    phone_number=forms.IntegerField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'phone_number','age','address')

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    age = forms.IntegerField()
    address=forms.CharField(widget=forms.Textarea)
    phone_number=forms.IntegerField()
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'phone_number','age','address')
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


class Addevent(forms.Form):
    name=forms.CharField(max_length=20)
    description=forms.CharField(widget=forms.Textarea)
    date=forms.DateField()
    time=forms.TimeField()
    # image=forms.ImageField()

    class Meta:
        model = Event
        fields = ('name','description','date','time')