from django.shortcuts import render

from recipe.models import Category, Recipe


def main(request):
    recipes = Recipe.objects.all()
    return render(request, 'main.html', {'recipes': recipes})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})