from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from engagement.emails import send_new_review_notification
from engagement.forms import ReviewForm
from engagement.models import Review

from .forms import ContactForm


def set_language(request, lang):
    if lang in ('cs', 'en'):
        request.session['site_lang'] = lang

    next_url = request.GET.get('next', '/')
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
        next_url = '/'
    return HttpResponseRedirect(next_url)


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'o-nas.html')


def cooperation(request):
    return render(request, 'spoluprace.html')


def fees(request):
    return render(request, 'odmena.html')


def references(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            send_new_review_notification(review)
            messages.success(request, 'Děkujeme za referenci. Bude publikována po schválení.')
            return redirect('references')
    else:
        form = ReviewForm()

    approved = Review.objects.filter(approved=True)
    average = None
    if approved.exists():
        average = round(sum(r.rating for r in approved) / approved.count(), 1)

    context = {
        'form': form,
        'submitted_reviews': approved,
        'average': average,
    }
    return render(request, 'reference.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Děkujeme, Vaše zpráva byla odeslána. Ozveme se co nejdříve.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'kontakt.html', {'form': form})


def privacy(request):
    return render(request, 'legal.html')
