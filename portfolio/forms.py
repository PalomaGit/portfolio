from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Asunto del mensaje'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 5
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
