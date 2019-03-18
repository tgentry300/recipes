from django.shortcuts import render
from django.http import HttpResponse
from .helpers import AllRecipes, RecipeDetails, AuthorDetails


def all_recipes(request, **kwargs):
    recipe_list = AllRecipes.get_all_recipes()
    return render(request, 'recipes.html.j2', {'recipes': recipe_list})


def recipe_details(request, recipe_id):
    recipe = RecipeDetails.get_recipe_by_id(recipe_id)
    return HttpResponse(render(request, 'recipedetails.html.j2', {'recipe': recipe}))


def author_details(request, author_name):
    author = AuthorDetails.get_author_details(author_name)
    authors_recipes = AuthorDetails.get_all_recipes_by_author(author)
    return HttpResponse(render(request, 'authordetails.html.j2', {'author': author, 'recipes': authors_recipes}))
