# Generated by Django 4.2.2 on 2023-06-18 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recipes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=30, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=200)),
                ('recipe_image', models.ImageField(upload_to=recipes.models.recipe_image_file_path)),
                ('meal_time', models.CharField(choices=[('b', 'Breakfast'), ('l', 'Lunch'), ('d', 'Dinner'), ('s', 'Snack')], max_length=1)),
                ('cost', models.CharField(choices=[('1', '£'), ('2', '££'), ('3', '£££'), ('4', '££££')], max_length=1)),
                ('instructions', models.TextField(max_length=800)),
                ('difficulty_level', models.CharField(choices=[('e', 'Easy'), ('m', 'Medium'), ('d', 'Difficult'), ('p', 'Pro')], max_length=1)),
                ('uploaded_date', models.DateField(auto_now_add=True)),
                ('visibility', models.CharField(choices=[('pr', 'Private'), ('pu', 'Public')], max_length=2)),
                ('ingredients', models.ManyToManyField(to='recipes.ingredient')),
                ('recipe_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='recipes.tag')),
            ],
        ),
    ]