from django import forms
from .models import Todo

class TudoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'deadline']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
