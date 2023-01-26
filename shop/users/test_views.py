from django.test import TestCase, Client

class TestUserCreate(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/users/create/')
        self.assertEqual(response.status_code, 200)

    def test_response_content(self):
        response = self.client.get('/users/create/')
        button = '<button type="submit">Registration</button>'.encode(encoding='utf-8')
        self.assertIn(button, response.content)

    def test_categories_as_guest(self):
        # guest
        response = self.client.get('/shop/categories/')
        self.assertEqual(response.status_code, 302)

    def test_ingredients_as_guest(self):
        # guest
        response = self.client.get('/shop/ingredients/')
        self.assertEqual(response.status_code, 302)
