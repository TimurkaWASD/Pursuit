from django import forms
from .models import *

class CreateTargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ['name', 'description', 'image', 'date_end', 'status', 'favorite', 'rating']
        widgets = { # Кроме того, для поля date_end мы используем виджет DateTimeInput с атрибутом type='datetime-local', чтобы пользователь мог выбирать дату и время.
            'date_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }