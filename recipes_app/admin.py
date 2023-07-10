from django.contrib import admin
from .models import Recipe, Ingredient, Category, Subcategory

# Register your models here.


@admin.register(Recipe)
class Recipe(admin.ModelAdmin):
    search_fields = ['category', 'title', ]
    list_display = ('id', 'title', 'preparation', 'image', 'preparation',
                    'preparation_time', 'type_cooking', 'oven_time',
                    'temperature',
                    )


@admin.register(Ingredient)
class Ingredient(admin.ModelAdmin):
    search_fields = ['recipe',]
    list_display = ('id', 'recipe', 'product', 'name', 'quantity',
                    'measure',
                    )


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)

    class Meta:
        verbose_name_plural = 'Categories'


@admin.register(Subcategory)
class Subcategory(admin.ModelAdmin):
    list_display = ('name',)

    class Meta:
        verbose_name_plural = 'Subcategories'
