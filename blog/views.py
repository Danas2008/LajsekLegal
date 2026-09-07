from django.shortcuts import get_object_or_404, render

from .models import BlogPost


def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    BlogPost.objects.filter(pk=post.pk).update(views=post.views + 1)
    return render(request, 'blog_detail.html', {'post': post})
