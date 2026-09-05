from django.shortcuts import render


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
    return render(request, 'kontakt.html')


def privacy(request):
    return render(request, 'legal.html')
