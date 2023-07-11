from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView
from .models import Recipe, Ingredient, Subcategory, Category

# Create your views here.


class RecipesList(ListView):
    """ VIEW FOR LIST ALL RECICPES """
    model = Recipe
    queryset = Recipe.objects.all()
    paginate_by = 4
    template_name = "recipes/recipes_list.html"


class RecipeDetail(View):
    model = Recipe
    template_name = "recipes/recipe_details.html"

    def get(self, request, id, *args, **kwargs):
        queryset = get_object_or_404(Recipe, pk=id)
