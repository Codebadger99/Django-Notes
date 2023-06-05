from django import forms
from .models import Notes


class NotesCreateForm(forms.ModelForm):
    heading = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-sm',
        'type': 'text',
        'aria-describedby':'helpId'
        }))
    
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control id_title',
        'rows':'3',
        'cols': '40',
        }))
     
    class Meta:
        model = Notes
        fields = '__all__'
