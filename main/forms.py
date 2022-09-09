from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import Profile
from django.conf import settings


class RegistrationForm(forms.ModelForm):
  username = forms.CharField(required=True, min_length=5, max_length=30)

  class Meta:
    model = User
    fields = ('username', 'email')
    
class UserRegisterForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  email    = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

    error_messages={
      "unique": "Wups, enter a unique username",
      'null': 'This field cannot be null.',
      'blank': 'This field cannot be blank.',
      'invalid' : 'Enter a valid email address.',
      'invalid_choice': 'Value is not a valid choice.',
      'required': 'This field is required.'}


attrs = {'class': 'form-control'}

class UserForm(forms.Form, forms.ModelForm):
  # The class 'form-control' is a bootstrap class
  username = forms.CharField(
    required = True, min_length = 4, max_length = 16,
    widget   = forms.TextInput(attrs=attrs),
    error_messages = {
      'required'  : "Korisničko ime je obavezno!",
      'max_length': "Username is longer than 16 characters.",
      'min_length': "Username is too short!",
    }
  )
  email    = forms.EmailField(widget=forms.EmailInput(attrs=attrs))
  password = forms.CharField(
    required = True, min_length = settings.MIN_PASSWORD_LENGHT,
    widget=forms.PasswordInput(attrs=attrs)
  )
  
  class Meta():
    model  = User
    fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
  image = forms.ImageField(
    required=False,
    widget=forms.FileInput(attrs={'class': 'form-control custom-file-input'})
  )

  class Meta():
    model  = Profile
    fields = ['image']

