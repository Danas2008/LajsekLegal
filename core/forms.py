from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Jméno a příjmení'}),
            'email': forms.EmailInput(attrs={'placeholder': 'vas@email.cz'}),
            'phone': forms.TextInput(attrs={'placeholder': '+420 000 000 000'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Předmět'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Vaše zpráva'}),
        }
        labels = {
            'name': 'Jméno',
            'email': 'E-mail',
            'phone': 'Telefon',
            'subject': 'Předmět',
            'message': 'Zpráva',
        }
