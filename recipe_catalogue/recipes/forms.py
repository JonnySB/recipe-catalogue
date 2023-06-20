from django import forms
from django.forms import ModelForm
from . import models


class AddRecipeForm(ModelForm):
    #recipe_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))

    class Meta:
        model = models.Recipe
        fields = ('recipe_name','recipe_image','meal_time',
                  'ingredients','cost','instructions',
                  'difficulty_level','tags','recipe_author','visibility')
        
        widgets = {
            'recipe_name':forms.TextInput(attrs={'class':'form-control'}),
            'meal_time':forms.Select(attrs={'class':'form-control'}),
            'ingredients':forms.SelectMultiple(attrs={'class':'form-control'}),
            'cost':forms.Select(attrs={'class':'form-control'}),
            'instructions':forms.Textarea(attrs={'class':'form-control'}),
            'difficulty_level':forms.Select(attrs={'class':'form-control'}),
            'tags':forms.SelectMultiple(attrs={'class':'form-control'}),
            'recipe_author':forms.HiddenInput(attrs={'class':'form-control'}),
            'visibility':forms.Select(attrs={'class':'form-control'}),
        }
        

        


