from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_request, name='logout'),
    path('pantry/', views.Pantry.as_view(), name='pantry'),
    path('pantry/addingredient/',
         views.AddIngredient.as_view(), name='create_ingredient'),
    path('pantry/<pk>/update/',
         views.UpdateIngredientView.as_view(), name='update_ingredient'),
    path('pantry/<pk>/delete/', views.DeleteIngredientView.as_view(),
         name='delete_ingredient'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('menu/addmenu/',
         views.AddMenu.as_view(), name='create_menu'),
    path('menu/<pk>/update/',
         views.UpdateMenuView.as_view(), name='update_menu'),
    path('menu/<pk>/delete/', views.DeleteMenuView.as_view(),
         name='delete_menu'),
]
