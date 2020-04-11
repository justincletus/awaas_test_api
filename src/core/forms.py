from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=120, required=True, help_text="Enter the username")
    email = forms.EmailField(max_length=254, help_text="Enter the valid email address")
    password1 = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    password2 = forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})

      
    class Meta:
        model = User
        fields = (
            'username',     
            'email',
            'password1',
            'password2'
            )
    
    def __init__(self, *args, **kargs):
        super(SignupForm, self).__init__(*args, **kargs)
