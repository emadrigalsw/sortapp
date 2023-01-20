from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Ingredient
from .forms import IngredientForm

# Create your views here.


def home(request):
    """
     Displays home page.

     **Template:**

     :template:`inventory/home.html`
     """
    context = {'text': 'Welcome to SortApp, your Deli manager'}
    return render(request, 'inventory/home.html', context)


class Pantry(ListView):
    """
    Displays the Pantry view, the list of elements.
    """
    model = Ingredient
    template_name = "inventory/pantry.html"


class AddIngredient(CreateView):
    """
    Creates a new ingredient with the corresponding model, template and form.
    """
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm
