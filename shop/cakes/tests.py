from django.test import TestCase
from .models import CakeType, Cake, Ingredient


# Create your tests here.
class TestCakeType(TestCase):

    def test_category_create(self):
        category = CakeType.objects.create(type='chocolate')
        self.assertEqual(str(category), 'chocolate')


class TestCake(TestCase):

    def setUp(self) -> None:
        self.category = CakeType.objects.create(type='chocolate')
        print('Before test')

    def tearDown(self) -> None:
        print('After test')

    def test_cake_creation(self):
        category = self.category
        cake = Cake.objects.create(
            name="New-York",
            type=category,
            price=20,
            weight=1,
        )
        self.assertEqual(str(cake), 'New-York (20$)')

    def test_ingred_add(self):
        category = self.category
        ingredient = Ingredient.objects.create(name='sugar')
        cake = Cake.objects.create(
            name="New-York",
            type=category,
            price=20,
            weight=1,
        )
        cake.ingredients.add(ingredient)
        self.assertTrue(isinstance(ingredient.name, str))
        self.assertEqual(cake.ingredients.all().first().name, 'sugar')


