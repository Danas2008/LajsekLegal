import datetime as dt
import json

from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .emails import send_booking_confirmation, send_booking_notification, send_new_review_notification
from .forms import BookingForm, NewsletterForm, ReviewForm
from .models import FAQ, Booking, Review


def available_slots():
    now = timezone.localtime()
    taken = set(
        Booking.objects.filter(
            status__in=[Booking.STATUS_PENDING, Booking.STATUS_CONFIRMED],
            datetime__gte=now,
        ).values_list('datetime', flat=True)
    )

    days = []
    for day_offset in range(settings.BOOKING_DAYS_AHEAD):
        day = (now + dt.timedelta(days=day_offset)).date()
        if day.weekday() not in settings.BOOKING_WEEKDAYS:
            continue

        day_slots = []
        for hour in settings.BOOKING_HOURS:
            slot_dt = timezone.make_aware(dt.datetime.combine(day, dt.time(hour=hour)))
            if slot_dt <= now:
                continue
            if slot_dt in taken:
                continue
            day_slots.append(slot_dt)

        if day_slots:
            days.append({'date': day, 'slots': day_slots})

    return days


def slots_by_date_json():
    data = {}
    for day in available_slots():
        data[day['date'].isoformat()] = [s.isoformat() for s in day['slots']]
    return json.dumps(data)


def booking(request):
    if request.method == 'POST':
        slot_raw = request.POST.get('slot')
        form = BookingForm(request.POST)
        slot_dt = None
        if slot_raw:
            try:
                parsed = dt.datetime.fromisoformat(slot_raw)
                slot_dt = timezone.make_aware(parsed) if timezone.is_naive(parsed) else parsed
            except ValueError:
                slot_dt = None

        slot_taken = slot_dt and Booking.objects.filter(
            datetime=slot_dt,
            status__in=[Booking.STATUS_PENDING, Booking.STATUS_CONFIRMED],
        ).exists()

        if not slot_dt:
            messages.error(request, 'Vyberte prosím termín schůzky.')
        elif slot_taken:
            messages.error(request, 'Tento termín je již obsazený, vyberte prosím jiný.')
        elif form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.datetime = slot_dt
            new_booking.save()
            send_booking_confirmation(new_booking)
            send_booking_notification(new_booking)
            messages.success(request, 'Schůzka rezervována. Potvrzení jsme poslali na Váš e-mail.')
            return redirect('booking')
    else:
        form = BookingForm()

    context = {
        'form': form,
        'days': available_slots(),
        'slots_json': slots_by_date_json(),
        'days_ahead': settings.BOOKING_DAYS_AHEAD,
    }
    return render(request, 'booking.html', context)


def recenze(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            send_new_review_notification(review)
            messages.success(request, 'Děkujeme za recenzi. Bude publikována po schválení.')
            return redirect('recenze')
    else:
        form = ReviewForm()

    approved = Review.objects.filter(approved=True)
    average = None
    if approved.exists():
        average = round(sum(r.rating for r in approved) / approved.count(), 1)

    context = {
        'form': form,
        'reviews': approved,
        'average': average,
    }
    return render(request, 'recenze.html', context)


def faq(request):
    context = {'faqs': FAQ.objects.filter(active=True)}
    return render(request, 'faq.html', context)


@csrf_exempt
@require_POST
def newsletter_subscribe(request):
    form = NewsletterForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'ok': True, 'message': 'Těšíme se, brzy pošleme novinky!'})
    return JsonResponse({'ok': False, 'errors': form.errors}, status=400)
