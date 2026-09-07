from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('o-nas/', views.about, name='about'),
    path('jak-probiha-spoluprace/', views.cooperation, name='cooperation'),
    path('odmena/', views.fees, name='fees'),
    path('reference/', views.references, name='references'),
    path('kontakt/', views.contact, name='contact'),
    path('osobni-udaje/', views.privacy, name='privacy'),
    path('jazyk/<str:lang>/', views.set_language, name='set_language'),
]
