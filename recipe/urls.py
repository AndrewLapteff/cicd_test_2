from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('categories/', views.category_list, name='category_list'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
]