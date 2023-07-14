from django.urls import path
from . import views

app_name = 'recipes_app'


urlpatterns = [
    path('', views.RecipesList.as_view(), name='recipes'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('success/', views.Success.as_view(), name='success_add_recipe'),
    path('add_ingredient/', views.AddIngredient.as_view(), name='add_ingredient'),
    path('<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]
