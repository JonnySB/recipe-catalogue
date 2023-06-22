from django import forms
from django.forms import ModelForm
from . import models


class AddRecipeForm(ModelForm):
    # recipe_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))

    class Meta:
        model = models.Recipe
        fields = ('recipe_name', 'recipe_image', 'meal_time',
                  'ingredients', 'cost', 'instructions',
                  'difficulty_level', 'tags', 'recipe_author', 'visibility')

        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'meal_time': forms.RadioSelect(attrs={'class': 'InLineRadios'}),
            'ingredients': forms.CheckboxSelectMultiple(attrs={'class': 'InlineRadios'}),
            'cost': forms.RadioSelect(attrs={'class': 'InlineRadios'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
            'difficulty_level': forms.RadioSelect(attrs={'class': 'InlineRadios'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'InlineRadios'}),
            'recipe_author': forms.HiddenInput(attrs={'class': 'form-control'}),
            'visibility': forms.RadioSelect(attrs={'class': 'InlineRadios'}),
        }

        labels = {
            'ingredients': 'Ingredients: (Note, more ingredients can be added on the subsequent page)',
            'instructions': 'Recipe method:',
            'tags': 'Tags: (Note, more tags can be added on the subsequent page)',
        }


class AddIngredientForm(ModelForm):

    class Meta:
        model = models.Ingredient
        fields = ('ingredient_name', 'user')
