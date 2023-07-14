from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView, ListView, CreateView, DetailView
from .models import Recipe, Ingredient, Subcategory, Category
from products.models import Spices
from .forms import AddRecipe, AddIngredient

# Create your views here.


class RecipesList(ListView):
    """ VIEW FOR LIST ALL RECICPES """
    model = Recipe
    queryset = Recipe.objects.all().order_by('title')
    paginate_by = 4
    template_name = "recipes_app/recipes_list.html"


class RecipeDetail(DetailView):
    model = Recipe


class AddRecipe(CreateView):
    form_class = AddRecipe
    template_name = "recipes_app/add_recipe.html"
    success_url = (f"../../recipes")
    message = "Success"


class AddIngredient(CreateView):
    form_class = AddIngredient
    template_name = "recipes_app/add_ingredient.html"
    success_url = (f"../../recipes/{{ recipe.id }}")
    message = 'success'
