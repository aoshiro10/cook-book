from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse

from app import models

# Create your views here.
def recipes(request):
    recipes = models.Recipe.objects.all()
    context = (
        RequestContext(
            request,
            {
                'recipes': recipes,
            }
        ).flatten()
    )
    return TemplateResponse(request, 'app/recipes.html', context=context)

def recipe(request, recipe_id):
    recipe = models.Recipe.objects.get(id=recipe_id)
    ingredients_list = recipe.ingredients.split("\n")
    for i in range(len(ingredients_list)):
        ingredient = ingredients_list[i]
        ingredient = ingredient.replace("\n", "")
        ingredients_list[i] = ingredient

    directions_list = recipe.directions.split("\n")
    for i in range(len(directions_list)):
        direction = directions_list[i]
        direction = direction.replace("\n", "")
        directions_list[i] = direction
    
    context = (
        RequestContext(
            request,
            {
                'directions': directions_list,
                'ingredients': ingredients_list,
                'recipe': recipe,
            }
        ).flatten()
    )
    return TemplateResponse(request, 'app/recipe.html', context=context)
