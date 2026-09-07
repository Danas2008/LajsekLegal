from django import forms

from .models import FAQ, Booking, NewsletterSubscriber, Review


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['client_name', 'email', 'phone', 'description']
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder': 'Jméno a příjmení'}),
            'email': forms.EmailInput(attrs={'placeholder': 'vas@email.cz'}),
            'phone': forms.TextInput(attrs={'placeholder': '+420 000 000 000'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Stručný popis Vašeho případu'}),
        }
        labels = {
            'client_name': 'Jméno',
            'email': 'E-mail',
            'phone': 'Telefon',
            'description': 'Popis',
        }


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')],
        widget=forms.RadioSelect,
        label='Hodnocení',
    )

    class Meta:
        model = Review
        fields = ['author', 'email', 'rating', 'text']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Jméno'}),
            'email': forms.EmailInput(attrs={'placeholder': 'vas@email.cz (nepovinné)'}),
            'text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Vaše zkušenost s naší kanceláří'}),
        }
        labels = {
            'author': 'Jméno',
            'email': 'E-mail',
            'text': 'Recenze',
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Váš e-mail'}),
        }
        labels = {'email': 'E-mail'}


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'active']
        widgets = {
            'question': forms.TextInput(attrs={'placeholder': 'Otázka'}),
            'answer': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Odpověď'}),
        }
        labels = {
            'question': 'Otázka',
            'answer': 'Odpověď',
            'active': 'Zveřejněno',
        }
