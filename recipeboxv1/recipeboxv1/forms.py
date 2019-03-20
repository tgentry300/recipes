from django import forms
from .models import Author


class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=20)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.IntegerField()


class UserAddForm(forms.Form):
    name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
