from django.shortcuts import render, redirect
from .models import Recipe
from .forms import AddRecipeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

# Create your views here.

def index(request):
    all_recipes = Recipe.objects.exclude(visibility__exact='pr').all()
    context = {'recipes':all_recipes}

    return render(request,'recipes/index.html',context=context)

@login_required
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, "Your recipe was successfully added!")
            return redirect('home')
    else:
        form = AddRecipeForm(initial={'recipe_author': request.user})

    return render(request, 'recipes/add_recipe.html', {'form':form})


class RecipeDetail(DetailView):
    model = Recipe


def recipe_detail(request):
    pass
        


