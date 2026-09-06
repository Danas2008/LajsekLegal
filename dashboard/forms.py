from django import forms

from blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'published_at', 'excerpt', 'body']
        widgets = {
            'published_at': forms.DateInput(attrs={'type': 'date'}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
            'body': forms.Textarea(attrs={'rows': 12}),
        }
