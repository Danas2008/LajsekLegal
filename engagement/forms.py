from django import forms

from .models import FAQ, Booking, BookingSettings, NewsletterSubscriber, Review

WEEKDAY_CHOICES = [
    (0, 'Pondělí'), (1, 'Úterý'), (2, 'Středa'), (3, 'Čtvrtek'),
    (4, 'Pátek'), (5, 'Sobota'), (6, 'Neděle'),
]

HOUR_CHOICES = [(h, f'{h:02d}:00') for h in range(7, 20)]


class BookingSettingsForm(forms.Form):
    weekdays = forms.MultipleChoiceField(
        choices=WEEKDAY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Dny, kdy přijímám schůzky',
    )
    hours = forms.MultipleChoiceField(
        choices=HOUR_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Časy schůzek (klienti si vybírají celou hodinu)',
    )
    days_ahead = forms.IntegerField(
        label='Kolik dní dopředu nabízet termíny',
        min_value=1,
        max_value=90,
    )

    def __init__(self, *args, instance=None, **kwargs):
        self.instance = instance
        initial = kwargs.pop('initial', {})
        if instance is not None:
            initial.setdefault('weekdays', [str(d) for d in instance.weekdays])
            initial.setdefault('hours', [str(h) for h in instance.hours])
            initial.setdefault('days_ahead', instance.days_ahead)
        super().__init__(*args, initial=initial, **kwargs)

    def save(self):
        self.instance.weekdays = sorted(int(d) for d in self.cleaned_data['weekdays'])
        self.instance.hours = sorted(int(h) for h in self.cleaned_data['hours'])
        self.instance.days_ahead = self.cleaned_data['days_ahead']
        self.instance.save()
        return self.instance


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
