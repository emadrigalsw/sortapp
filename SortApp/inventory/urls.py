from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pantry/', views.Pantry.as_view(), name='pantry'),
    path('pantry/addingredient/',
         views.AddIngredient.as_view(), name='create_ingredient'),
    path('pantry/<pk>/update/',
         views.UpdateIngredientView.as_view(), name='update_ingredient'),
    path('pantry/<pk>/delete/', views.DeleteIngredientView.as_view(),
         name='delete_ingredient'),
]
