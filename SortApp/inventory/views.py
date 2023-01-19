from django.shortcuts import render
from django.views.generic import ListView
from .models import Ingredient

# Create your views here.


def home(request):
    context = {'text': 'Welcome to SortApp, your Deli manager'}
    return render(request, 'inventory/home.html', context)


class Pantry(ListView):
    model = Ingredient
    template_name = "inventory/pantry.html"
