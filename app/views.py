from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.response import TemplateResponse
from django.http import JsonResponse

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
    ingredients_list = recipe.ingredients.split("\\n")
    for i in range(len(ingredients_list)):
        ingredient = ingredients_list[i]
        ingredient = ingredient.replace("\\n", "")
        ingredients_list[i] = ingredient

    directions_list = recipe.directions.split("\\n")
    for i in range(len(directions_list)):
        direction = directions_list[i]
        direction = direction.replace("\\n", "")
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

def filter(request):
    text_filter = request.GET.get('filter_text')
    recipes = models.Recipe.filter_recipe(text_filter)
    recipes_html = ""
    if recipes:
        recipes_html = loader.render_to_string('app/recipes_list.html', {'recipes': recipes})

    response_data = {
        'recipes_html': recipes_html
    }
    return JsonResponse(response_data)