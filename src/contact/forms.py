from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Your name"}))
    email = forms.EmailField(label='',
                           widget=forms.TextInput(attrs={"placeholder": "Your email"}))
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Message",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                'cols': 120
            }
        )
    )

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'message'
        ]