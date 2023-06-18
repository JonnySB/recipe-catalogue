from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, Tag

# Create your views here.

def index(request):
    all_recipes = Recipe.objects.all()
    context = {'recipes':all_recipes}

    return render(request,'recipes/index.html',context=context)