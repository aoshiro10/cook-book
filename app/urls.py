from django.urls import path

from . import views

urlpatterns = [
    path('<int:recipe_id>/', views.recipe, name='recipe'),
    path('', views.recipes, name='recipes'),
    path('lazy_filter/', views.filter, name='filter')
]