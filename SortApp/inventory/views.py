from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Ingredient
from .forms import IngredientForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
from django.contrib.auth import logout


# Create your views here.


def index(request):
    """
     Displays home page.

     **Template:**

     :template:`inventory/home.html`
     """
    context = {
        'text': 'Welcome to SortApp, your Deli manager, please Log in to use the app.'}
    return render(request, 'inventory/index.html', context)


def logout_request(request):

    logout(request)
    return redirect('index')


class Pantry(LoginRequiredMixin, ListView):
    """
    Displays the Pantry view, the list of ingredients.
    """

    model = Ingredient
    template_name = "inventory/pantry.html"


class AddIngredient(CreateView):
    """
    Creates a new ingredient, with the corresponding model, template and form.
    """
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm


class UpdateIngredientView(UpdateView):
    """
    Changes an existent ingredient, with the corresponding model, template and form.
    """
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientForm


class DeleteIngredientView(DeleteView):
    """
    Deletes an existent ingredient, with the corresponding model, template and form.
    """
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = "/pantry"
