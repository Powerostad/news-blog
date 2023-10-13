from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class HomePageTest(SimpleTestCase):
    def test_url_exists_at_correct_location_homepageview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        respons = self.client.get(reverse("home"))
        self.assertEqual(respons.status_code, 200)
        self.assertTemplateUsed(respons, "home.html")
        self.assertContains(respons, "Home")
