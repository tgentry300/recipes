from django.shortcuts import render

recipes = ['food', 'mor foods', 'pizza']


def all_recipes(request, **kwargs):
    return render(request, 'recipes.html.j2', {'recipes': recipes})


def recipe_details(request, **kwargs):
    return render(request, 'recipedetails.html.j2')


def author_details(request, **kwargs):
    return render(request, 'authordetails.html.j2')
