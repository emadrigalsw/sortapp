from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Ingredient
from .forms import IngredientForm

# Create your views here.


def home(request):
    context = {'text': 'Welcome to SortApp, your Deli manager'}
    return render(request, 'inventory/home.html', context)


class Pantry(ListView):
    model = Ingredient
    template_name = "inventory/pantry.html"


class CreateIngredient(CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm
