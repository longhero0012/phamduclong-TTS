from django.http import response
from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase) :
    def test_web_page_status(self) : 
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)