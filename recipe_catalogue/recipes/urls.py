from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe_detail/<int:pk>',views.RecipeDetail.as_view(),name='recipe_detail'),
]
