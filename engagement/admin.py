from django.contrib import admin

from .models import FAQ, Booking, NewsletterSubscriber, Review


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'datetime', 'status', 'email', 'phone')
    list_filter = ('status',)
    ordering = ('datetime',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'approved', 'created_at')
    list_filter = ('approved', 'rating')
    ordering = ('-created_at',)


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'active')
    ordering = ('-subscribed_at',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'active')
    ordering = ('order',)
