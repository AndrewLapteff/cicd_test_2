from django.test import Client, TestCase
from django.urls import reverse

from recipe.models import Category, Recipe


class ModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            instructions='Test Instructions',
            ingredients='Test Ingredients',
            category=self.category
        )

    def test_category_creation(self):
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(self.category.name, 'Test Category')

    def test_recipe_creation(self):
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(self.recipe.title, 'Test Recipe')
        self.assertEqual(self.recipe.description, 'Test Description')
        self.assertEqual(self.recipe.instructions, 'Test Instructions')
        self.assertEqual(self.recipe.ingredients, 'Test Ingredients')
        self.assertEqual(self.recipe.category, self.category)

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            instructions='Test Instructions',
            ingredients='Test Ingredients',
            category=self.category
        )

    def test_recipe_list_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Category')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')