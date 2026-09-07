from django.urls import path

from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('faq/', views.faq, name='faq'),
    path('newsletter/prihlasit/', views.newsletter_subscribe, name='newsletter_subscribe'),
]
