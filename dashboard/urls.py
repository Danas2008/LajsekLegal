from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/novy/', views.blog_create, name='blog_create'),
    path('blog/<slug:slug>/upravit/', views.blog_edit, name='blog_edit'),
    path('blog/<slug:slug>/smazat/', views.blog_delete, name='blog_delete'),
    path('api/text/', views.save_text, name='save_text'),
]
