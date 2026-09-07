from django.conf import settings
from django.core.mail import send_mail


def send_booking_confirmation(booking):
    send_mail(
        subject='Rezervace schůzky – Lajsek Legal',
        message=(
            f'Dobrý den {booking.client_name},\n\n'
            f'Vaše schůzka byla rezervována na {booking.datetime:%d.%m.%Y v %H:%M}.\n'
            'Jakmile ji potvrdíme, dostanete zprávu.\n\n'
            'S pozdravem,\nLajsek Legal'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[booking.email],
        fail_silently=True,
    )


def send_booking_notification(booking):
    send_mail(
        subject='Nová rezervace schůzky',
        message=(
            f'Nová rezervace od {booking.client_name} ({booking.email}, {booking.phone}).\n'
            f'Termín: {booking.datetime:%d.%m.%Y v %H:%M}\n\n'
            f'Popis:\n{booking.description}'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_NOTIFICATION_EMAIL],
        fail_silently=True,
    )


def send_new_review_notification(review):
    send_mail(
        subject='Nová recenze čeká na schválení',
        message=(
            f'Autor: {review.author}\n'
            f'Hodnocení: {review.rating}/5\n\n'
            f'{review.text}'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_NOTIFICATION_EMAIL],
        fail_silently=True,
    )
