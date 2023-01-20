from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pantry/', views.Pantry.as_view(), name='pantry'),
    path('pantry/addingredient/',
         views.AddIngredient.as_view(), name='create_ingredient'),
]
