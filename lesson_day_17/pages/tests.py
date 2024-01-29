# from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
class HomepageTests(SimpleTestCase):
     def test_url_exists_at_correct_location(self):
         response = self.client.get("/")
         self.assertEqual(response.status_code, 200)
         
class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

class InfopageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/info/")
        self.assertEqual(response.status_code, 200)