from django.shortcuts import get_object_or_404, render

from recipe.models import Category, Recipe


def main(request):
    recipes = Recipe.objects.all()
    return render(request, 'main.html', {'recipes': recipes})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})