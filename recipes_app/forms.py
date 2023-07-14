from django import forms
from .models import Recipe, Subcategory, Category, Ingredient


class AddRecipe(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'subcategory', 'category', 'image', 'preparation',
                  'preparation_time', 'type_cooking', 'oven_time',
                  'temperature',)


class AddIngredient(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('recipe', 'product', 'name', 'quantity', 'measure',)
