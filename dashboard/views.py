from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import BlogPost

from .forms import BlogPostForm


@staff_member_required
def home(request):
    return render(request, 'dashboard/home.html')


@staff_member_required
def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'dashboard/blog_list.html', {'posts': posts})


@staff_member_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
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
