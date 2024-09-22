from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def faq(request):
    return render(request, 'main/faq.html')


def pricing(request):
    return render(request, 'main/pricing.html')


def terms(request):
    return render(request, 'main/tnc.html')


def priv_pol(request):
    return render(request, 'main/priv-pol.html')
