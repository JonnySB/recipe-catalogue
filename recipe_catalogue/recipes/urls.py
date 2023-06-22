from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_additional_ingredients/<int:pk>',
         views.add_additional_ingredients, name='add_additional_ingredients'),
    path('recipe_detail/<int:pk>',
         views.RecipeDetail.as_view(), name='recipe_detail'),
]
