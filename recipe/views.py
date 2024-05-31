from django.shortcuts import render

from recipe.models import Recipe


def main(request):
    recipes = Recipe.objects.all()
    return render(request, 'main.html', {'recipes': recipes})