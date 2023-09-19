import os
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

os.pardir


def recipe_image_file_path(instance, filename):
    '''Generate filepath for new recipe_image'''
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}{ext}"
    return os.path.join('uploads', 'recipe', filename)


class Recipe(models.Model):

    recipe_name = models.CharField(max_length=200)
    recipe_image = models.ImageField(upload_to=recipe_image_file_path)

    MEAL_TIME_CHOICES = [
        ('b', 'Breakfast'),
        ('l', 'Lunch'),
        ('d', 'Dinner'),
        ('s', 'Snack'),
    ]
    meal_time = models.CharField(
        max_length=1, choices=MEAL_TIME_CHOICES, default='b')

    ingredients = models.ManyToManyField('Ingredient')

    COST_CHOICES = [
        ('1', '£'),
        ('2', '££'),
        ('3', '£££'),
        ('4', '££££'),
    ]
    cost = models.CharField(max_length=1, choices=COST_CHOICES, default='1')

    instructions = models.TextField(max_length=800)

    DIFFICULTY_CHOICES = [
        ('e', 'Easy'),
        ('m', 'Medium'),
        ('d', 'Difficult'),
        ('p', 'Pro'),
    ]
    difficulty_level = models.CharField(max_length=1,
                                        choices=DIFFICULTY_CHOICES,
                                        default='e')

    tags = models.ManyToManyField('Tag')
    recipe_author = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_date = models.DateField(auto_now_add=True)

    VISIBILITY_CHOICES = [
        ('pu', 'Public'),
        ('pr', 'Private'),
    ]
    visibility = models.CharField(
        max_length=2, choices=VISIBILITY_CHOICES, default='pu')

    def __str__(self):
        return self.recipe_name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['ingredient_name']

    def __str__(self):
        return self.ingredient_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name
