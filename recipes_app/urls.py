from django.urls import path
from . import views

app_name = 'recipes'


urlpatterns = [
    path('', views.RecipesList.as_view(), name='recipes'),
    path('<int:id>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]
