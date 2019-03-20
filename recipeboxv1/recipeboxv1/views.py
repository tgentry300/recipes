from django.shortcuts import render, HttpResponseRedirect, reverse
from .helpers import AllRecipes, RecipeDetails, AuthorDetails
from .models import Recipe, Author
from .forms import AuthorAddForm, RecipeAddForm, UserAddForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


def all_recipes(request, **kwargs):
    recipe_list = AllRecipes.get_all_recipes()
    return render(request, 'recipes.html.j2', {'recipes': recipe_list})


@login_required()
def recipe_details(request, recipe_id):
    recipe = RecipeDetails.get_recipe_by_id(recipe_id)
    return render(request, 'recipedetails.html.j2', {'recipe': recipe})


@login_required()
def author_details(request, author_name):
    author = AuthorDetails.get_author_details(author_name)
    authors_recipes = AuthorDetails.get_all_recipes_by_author(author)
    return render(request, 'authordetails.html.j2', {'author': author, 'recipes': authors_recipes})


def author_add(request):
    html = 'generic_form.html.j2'
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


@login_required()
def recipe_add(request):
    html = 'generic_form.html.j2'
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


def signup_view(request):
    html = 'generic_form.html.j2'
    form = None

    if request.method == 'POST':
        form = UserAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            new_user = User.objects.create(
                username=data['username'],
                password=data['password']
            )
            Author.objects.create(
                name=data['name'],
                user=new_user
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))

    else:
        form = UserAddForm()

    return render(request, html, {'form': form})


def login_view(request):
    html = 'generic_form.html.j2'

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(username=data['username'], password=data['password'])
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(request.GET.get('next', '/'))
    else:
        form = LoginForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
