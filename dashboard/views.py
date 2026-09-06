import json

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify
from django.views.decorators.http import require_POST

from blog.models import BlogPost
from core.models import TextBlock

from .forms import BlogPostForm


def unique_slug(title, exclude_pk=None):
    base = slugify(title) or 'clanek'
    slug = base
    qs = BlogPost.objects.all()
    if exclude_pk:
        qs = qs.exclude(pk=exclude_pk)
    counter = 2
    while qs.filter(slug=slug).exists():
        slug = f'{base}-{counter}'
        counter += 1
    return slug


def clanek_word(count):
    if count == 1:
        return 'článek'
    if 2 <= count <= 4:
        return 'články'
    return 'článků'


@staff_member_required
def home(request):
    post_count = BlogPost.objects.count()
    return render(request, 'dashboard/home.html', {
        'post_count': post_count,
        'clanek_word': clanek_word(post_count),
    })


@staff_member_required
def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'dashboard/blog_list.html', {'posts': posts})


@staff_member_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = unique_slug(post.title)
            post.save()
            messages.success(request, 'Článek byl vytvořen.')
            return redirect('dashboard:blog_list')
    else:
        form = BlogPostForm()

    return render(request, 'dashboard/blog_form.html', {'form': form, 'title': 'Nový článek'})


@staff_member_required
def blog_edit(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Článek byl uložen.')
            return redirect('dashboard:blog_list')
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'dashboard/blog_form.html', {'form': form, 'title': 'Upravit článek', 'post': post})


@staff_member_required
def blog_delete(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Článek byl smazán.')
        return redirect('dashboard:blog_list')

    return render(request, 'dashboard/blog_confirm_delete.html', {'post': post})


@staff_member_required
@require_POST
def save_text(request):
    data = json.loads(request.body)
    key = data.get('key', '').strip()
    content = data.get('content', '')
    if not key:
        return JsonResponse({'ok': False, 'error': 'missing key'}, status=400)

    TextBlock.objects.update_or_create(key=key, defaults={'content': content})
    return JsonResponse({'ok': True})
