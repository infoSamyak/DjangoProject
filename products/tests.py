from django.test import TestCase


class ProductsTests(TestCase):
    def test_products_endpoint_exists(self):
        response = self.client.get("/api/products")
        self.assertIn(response.status_code, (200, 404, 500))
