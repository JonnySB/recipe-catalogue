from django.shortcuts import render, redirect
from .models import Recipe, Ingredient
from .forms import AddRecipeForm, AddIngredientForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.http import HttpResponse

# Create your views here.


def index(request):
    all_recipes = Recipe.objects.exclude(visibility__exact='pr').all()
    context = {'recipes': all_recipes}

    return render(request, 'recipes/index.html', context=context)


@login_required
def private_feed(request):
    users_recipes = Recipe.objects.filter(recipe_author__exact=request.user)
    context = {'recipes': users_recipes}

    return render(request, 'recipes/private_feed.html', context)


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            messages.success(request, "Your recipe was successfully added!")

            print(recipe.pk)
            return redirect('add_additional_ingredients', recipe.pk)
    else:
        form = AddRecipeForm(initial={'recipe_author': request.user})

    return render(request, 'recipes/add_recipe.html', {'form': form})


@login_required
def add_additional_ingredients(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = AddIngredientForm()
    if request.method == 'POST':
        form = AddIngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save()
            recipe.ingredients.add(ingredient)
            return redirect('add_additional_ingredients', recipe.pk)

    context = {'form': form, 'recipe': recipe}

    return render(request, 'recipes/add_additional_ingredients.html', context)


class RecipeDetail(DetailView):
    model = Recipe
