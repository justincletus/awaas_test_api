from django.contrib.auth.forms import UserCreationForm
from .models import Student, User, Course
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2']
        help_texts = {
            'username': 'same as your roll no.',
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'user',
            'student_name',
            'father_name',
            'email',
            'enrollment_no',
            'course',
            'dob',
            'gender']


class SelectionForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['room']


class DuesForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Student.objects.all().filter(no_dues=True))


class NoDuesForm(forms.Form):
    choice = forms.ModelChoiceField(queryset=Student.objects.all().filter(no_dues=False))
