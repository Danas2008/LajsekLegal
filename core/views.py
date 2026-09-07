from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

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
    return render(request, 'reference.html')


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
