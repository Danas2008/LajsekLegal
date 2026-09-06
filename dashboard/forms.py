from django import forms

from blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'published_at', 'excerpt', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Název článku'}),
            'published_at': forms.DateInput(attrs={'type': 'date'}),
            'excerpt': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Krátký úvodní text zobrazený ve výpisu'}),
            'body': forms.Textarea(attrs={'rows': 14, 'placeholder': 'Text celého článku'}),
        }
        labels = {
            'title': 'Název',
            'published_at': 'Datum vydání',
            'excerpt': 'Úvodní text (perex)',
            'body': 'Text článku',
        }
