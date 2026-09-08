import csv
import json

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.text import slugify
from django.views.decorators.http import require_POST

from blog.models import BlogPost
from core.models import ContactMessage, TextBlock
from engagement.forms import BookingSettingsForm, FAQForm
from engagement.models import FAQ, Booking, BookingSettings, NewsletterSubscriber, Review

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
    now = timezone.localtime()
    tomorrow_end = (now + timezone.timedelta(days=2)).replace(hour=0, minute=0, second=0, microsecond=0)

    context = {
        'post_count': BlogPost.objects.count(),
        'clanek_word': clanek_word(BlogPost.objects.count()),
        'upcoming_bookings': Booking.objects.filter(
            datetime__gte=now, datetime__lt=tomorrow_end,
        ).exclude(status=Booking.STATUS_CANCELLED).order_by('datetime'),
        'unresolved_contacts': ContactMessage.objects.filter(status=ContactMessage.STATUS_NEW).count(),
        'pending_reviews': Review.objects.filter(approved=False).count(),
        'newsletter_count': NewsletterSubscriber.objects.filter(active=True).count(),
        'top_posts': BlogPost.objects.order_by('-views')[:5],
    }
    return render(request, 'dashboard/home.html', context)


# --- Blog -------------------------------------------------------------

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


# --- Bookings -----------------------------------------------------------

@staff_member_required
def booking_list(request):
    now = timezone.localtime()
    status_filter = request.GET.get('filter', 'upcoming')

    bookings = Booking.objects.all()
    if status_filter == 'upcoming':
        bookings = bookings.filter(datetime__gte=now).exclude(status=Booking.STATUS_CANCELLED)
    elif status_filter == 'past':
        bookings = bookings.filter(datetime__lt=now)
    elif status_filter == 'pending':
        bookings = bookings.filter(status=Booking.STATUS_PENDING)

    return render(request, 'dashboard/booking_list.html', {
        'bookings': bookings,
        'status_filter': status_filter,
    })


@staff_member_required
@require_POST
def booking_confirm(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.status = Booking.STATUS_CONFIRMED
    booking.save(update_fields=['status'])
    messages.success(request, 'Schůzka byla potvrzena.')
    return redirect('dashboard:booking_list')


@staff_member_required
@require_POST
def booking_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.status = Booking.STATUS_CANCELLED
    booking.save(update_fields=['status'])
    messages.success(request, 'Schůzka byla zrušena.')
    return redirect('dashboard:booking_list')


@staff_member_required
def booking_settings(request):
    instance = BookingSettings.load()
    if request.method == 'POST':
        form = BookingSettingsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nastavení termínů bylo uloženo.')
            return redirect('dashboard:booking_settings')
    else:
        form = BookingSettingsForm(instance=instance)

    return render(request, 'dashboard/booking_settings.html', {'form': form})


# --- Contact submissions --------------------------------------------------

@staff_member_required
def contact_list(request):
    status_filter = request.GET.get('filter', 'new')
    contacts = ContactMessage.objects.all()
    if status_filter in dict(ContactMessage.STATUS_CHOICES):
        contacts = contacts.filter(status=status_filter)

    return render(request, 'dashboard/contact_list.html', {
        'contacts': contacts,
        'status_filter': status_filter,
    })


@staff_member_required
@require_POST
def contact_resolve(request, pk):
    contact = get_object_or_404(ContactMessage, pk=pk)
    contact.status = ContactMessage.STATUS_RESOLVED
    contact.save(update_fields=['status'])
    messages.success(request, 'Zpráva byla označena jako vyřešená.')
    return redirect('dashboard:contact_list')


@staff_member_required
@require_POST
def contact_archive(request, pk):
    contact = get_object_or_404(ContactMessage, pk=pk)
    contact.status = ContactMessage.STATUS_ARCHIVED
    contact.save(update_fields=['status'])
    messages.success(request, 'Zpráva byla archivována.')
    return redirect('dashboard:contact_list')


@staff_member_required
@require_POST
def contact_delete(request, pk):
    contact = get_object_or_404(ContactMessage, pk=pk)
    contact.delete()
    messages.success(request, 'Zpráva byla smazána.')
    return redirect('dashboard:contact_list')


@staff_member_required
def contact_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="kontakty.csv"'
    writer = csv.writer(response)
    writer.writerow(['Datum', 'Jméno', 'E-mail', 'Telefon', 'Předmět', 'Zpráva', 'Status'])
    for contact in ContactMessage.objects.all():
        writer.writerow([
            contact.created_at.strftime('%d.%m.%Y %H:%M'),
            contact.name, contact.email, contact.phone,
            contact.subject, contact.message, contact.get_status_display(),
        ])
    return response


# --- Reviews --------------------------------------------------------------

@staff_member_required
def review_list(request):
    status_filter = request.GET.get('filter', 'pending')
    reviews = Review.objects.all()
    if status_filter == 'pending':
        reviews = reviews.filter(approved=False)
    elif status_filter == 'approved':
        reviews = reviews.filter(approved=True)

    approved_qs = Review.objects.filter(approved=True)
    average = None
    if approved_qs.exists():
        average = round(sum(r.rating for r in approved_qs) / approved_qs.count(), 1)

    return render(request, 'dashboard/review_list.html', {
        'reviews': reviews,
        'status_filter': status_filter,
        'average': average,
        'approved_count': approved_qs.count(),
    })


@staff_member_required
@require_POST
def review_approve(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.approved = True
    review.save(update_fields=['approved'])
    messages.success(request, 'Recenze byla schválena.')
    return redirect('dashboard:review_list')


@staff_member_required
@require_POST
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    messages.success(request, 'Recenze byla smazána.')
    return redirect('dashboard:review_list')


# --- Newsletter -------------------------------------------------------------

@staff_member_required
def newsletter_list(request):
    subscribers = NewsletterSubscriber.objects.all()
    return render(request, 'dashboard/newsletter_list.html', {
        'subscribers': subscribers,
        'active_count': subscribers.filter(active=True).count(),
    })


@staff_member_required
def newsletter_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="newsletter.csv"'
    writer = csv.writer(response)
    writer.writerow(['E-mail', 'Přihlášen', 'Aktivní'])
    for sub in NewsletterSubscriber.objects.all():
        writer.writerow([sub.email, sub.subscribed_at.strftime('%d.%m.%Y %H:%M'), 'Ano' if sub.active else 'Ne'])
    return response


# --- FAQ --------------------------------------------------------------------

@staff_member_required
def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'dashboard/faq_list.html', {'faqs': faqs})


@staff_member_required
def faq_create(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.order = (FAQ.objects.order_by('-order').values_list('order', flat=True).first() or 0) + 1
            faq.save()
            messages.success(request, 'Otázka byla přidána.')
            return redirect('dashboard:faq_list')
    else:
        form = FAQForm()

    return render(request, 'dashboard/faq_form.html', {'form': form, 'title': 'Nová otázka'})


@staff_member_required
def faq_edit(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Otázka byla uložena.')
            return redirect('dashboard:faq_list')
    else:
        form = FAQForm(instance=faq)

    return render(request, 'dashboard/faq_form.html', {'form': form, 'title': 'Upravit otázku', 'faq': faq})


@staff_member_required
@require_POST
def faq_delete(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    faq.delete()
    messages.success(request, 'Otázka byla smazána.')
    return redirect('dashboard:faq_list')


@staff_member_required
@require_POST
def faq_move(request, pk, direction):
    faq = get_object_or_404(FAQ, pk=pk)
    if direction == 'up':
        neighbor = FAQ.objects.filter(order__lt=faq.order).order_by('-order').first()
    else:
        neighbor = FAQ.objects.filter(order__gt=faq.order).order_by('order').first()

    if neighbor:
        faq.order, neighbor.order = neighbor.order, faq.order
        faq.save(update_fields=['order'])
        neighbor.save(update_fields=['order'])

    return redirect('dashboard:faq_list')


# --- Editable text API ------------------------------------------------------

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
