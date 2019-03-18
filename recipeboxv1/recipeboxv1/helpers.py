from .models import Author, Recipe
# from django.contrib.auth.models import User


class AllRecipes:
    """Class get's all recipes from database"""
    def get_all_recipes():
        return Recipe.objects.all()


class RecipeDetails:
    """Class get's recipe details"""
    def get_recipe_by_id(recipe_id):
        return Recipe.objects.get(id=recipe_id)


class AuthorDetails:
    """Class get's author details"""
    def get_author_details(author_name):
        return Author.objects.get(name=author_name)

    def get_all_recipes_by_author(author):
        return Recipe.objects.filter(author=author)
