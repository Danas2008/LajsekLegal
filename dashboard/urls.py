from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),

    path('blog/', views.blog_list, name='blog_list'),
    path('blog/novy/', views.blog_create, name='blog_create'),
    path('blog/<slug:slug>/upravit/', views.blog_edit, name='blog_edit'),
    path('blog/<slug:slug>/smazat/', views.blog_delete, name='blog_delete'),

    path('schuzky/', views.booking_list, name='booking_list'),
    path('schuzky/<int:pk>/potvrdit/', views.booking_confirm, name='booking_confirm'),
    path('schuzky/<int:pk>/zrusit/', views.booking_cancel, name='booking_cancel'),

    path('formulare/', views.contact_list, name='contact_list'),
    path('formulare/<int:pk>/vyresit/', views.contact_resolve, name='contact_resolve'),
    path('formulare/<int:pk>/archivovat/', views.contact_archive, name='contact_archive'),
    path('formulare/<int:pk>/smazat/', views.contact_delete, name='contact_delete'),
    path('formulare/export/', views.contact_export, name='contact_export'),

    path('recenze/', views.review_list, name='review_list'),
    path('recenze/<int:pk>/schvalit/', views.review_approve, name='review_approve'),
    path('recenze/<int:pk>/smazat/', views.review_delete, name='review_delete'),

    path('newsletter/', views.newsletter_list, name='newsletter_list'),
    path('newsletter/export/', views.newsletter_export, name='newsletter_export'),

    path('faq/', views.faq_list, name='faq_list'),
    path('faq/nova/', views.faq_create, name='faq_create'),
    path('faq/<int:pk>/upravit/', views.faq_edit, name='faq_edit'),
    path('faq/<int:pk>/smazat/', views.faq_delete, name='faq_delete'),
    path('faq/<int:pk>/posun/<str:direction>/', views.faq_move, name='faq_move'),

    path('api/text/', views.save_text, name='save_text'),
]
