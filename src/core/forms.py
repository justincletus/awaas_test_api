from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text="Enter the valid email address")
    birth_date = forms.DateField(help_text='Required. Format: yyyy-mm-dd')
    class Meta:
        model = User
        fields = ('username', 'birth_date', 'first_name', 'last_name', 'email', 'password1', 'password2')

