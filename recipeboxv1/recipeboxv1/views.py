from django.shortcuts import render
from .helpers import AllRecipes, RecipeDetails, AuthorDetails
from .models import Recipe, Author
from .forms import AuthorAddForm, RecipeAddForm
from django.contrib.auth.models import User



def all_recipes(request, **kwargs):
    recipe_list = AllRecipes.get_all_recipes()
    return render(request, 'recipes.html.j2', {'recipes': recipe_list})


def recipe_details(request, recipe_id):
    recipe = RecipeDetails.get_recipe_by_id(recipe_id)
    return render(request, 'recipedetails.html.j2', {'recipe': recipe})


def author_details(request, author_name):
    author = AuthorDetails.get_author_details(author_name)
    authors_recipes = AuthorDetails.get_all_recipes_by_author(author)
    return render(request, 'authordetails.html.j2', {'author': author, 'recipes': authors_recipes})


def author_add(request):
    html = 'authoradd.html.j2'
    form = None

    if request.method == "POST":
        form = AuthorAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            new_user = User.objects.create(
                username=data['name'],
            )

            Author.objects.create(
                name=data['name'],
                user=new_user,
                bio=data['bio']
            )
            return render(request, 'thanks.html.j2')
    else:
        form = AuthorAddForm()

    return render(request, html, {'form': form})


def recipe_add(request):
    html = 'recipeadd.html.j2'
    form = None

    if request.method == 'POST':
        form = RecipeAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required']
            )
            return render(request, 'thanks.html.j2')

    else:
        form = RecipeAddForm()

    return render(request, html, {'form': form})
