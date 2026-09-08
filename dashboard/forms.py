from django import forms

from blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'published_at', 'cover_image', 'excerpt', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Název článku'}),
            'published_at': forms.DateInput(attrs={'type': 'date'}),
            'cover_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'excerpt': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Krátký úvodní text zobrazený ve výpisu'}),
            'body': forms.Textarea(attrs={'rows': 14, 'placeholder': 'Text celého článku'}),
        }
        labels = {
            'title': 'Název',
            'published_at': 'Datum vydání',
            'cover_image': 'Titulní obrázek',
            'excerpt': 'Úvodní text (perex)',
            'body': 'Text článku',
        }
