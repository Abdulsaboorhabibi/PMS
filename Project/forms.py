from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': 'Enter project title', 'ColSpan': '2'}),
            'province': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter province'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter district'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'ColSpan': '2', 'placeholder': 'Enter project description', 'rows': 3 }),
        }