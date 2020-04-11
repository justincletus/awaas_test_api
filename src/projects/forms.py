from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                'cols': 120
            }
        )
    )

    class Meta:
        model = Project
        fields = [
            'title',
            'description',
        ]