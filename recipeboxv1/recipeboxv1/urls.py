"""recipeboxv1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_recipes, name='home'),
    path('authordetails/<str:author_name>', views.author_details),
    path('recipedetails/<int:recipe_id>', views.recipe_details),
    path('authoradd', views.author_add),
    path('recipeadd', views.recipe_add),
    path('login/', views.login_view),
    path('signup', views.signup_view),
    path('logout/', views.logout_view)
]
