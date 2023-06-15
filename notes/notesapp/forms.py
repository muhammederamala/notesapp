from django import forms
from .models import note_model

class note_form(forms.ModelForm):
    class Meta:
        model = note_model
        fields = ['text', 'audio', 'video']
