from django.test import TestCase, Client


class TestCakeListView(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/shop/cakes/')
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        response = self.client.get('/shop/cakes/')
        self.assertIn('help_text', response.context)
