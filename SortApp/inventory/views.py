from django.shortcuts import render

# Create your views here.


def home(request):
    context = {'text': 'Welcome to SortApp, your Deli manager'}
    return render(request, 'inventory/home.html', context)
