from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class XTestCase(TestCase):
    # HTTPステータスコードが200になるかどうか
    def test_response_200(self):
        x_url = reverse("tyuusenn:Login")
        detail_response = self.client.get(x_url)
        self.assertEqual(detail_response.status_code, 200)

    # HTTPステータスコードが302になるかどうか
    def test_response_302(self):
        x_url = reverse("tyuusenn:Logout")
        detail_response = self.client.get(x_url)
        self.assertEqual(detail_response.status_code, 302)
