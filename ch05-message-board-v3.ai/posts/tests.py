from django.test import TestCase
from django.urls import reverse

from .models import Post


class HomePageTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_posts_render_on_homepage(self):
        response = self.client.get(reverse("home"))
        for text in [
            "Merhaba, bu ilk örnek mesaj.",
            "Django ile basit bir mesaj panosu.",
            "Üçüncü mesaj da burada görünecek.",
        ]:
            self.assertContains(response, text)

# Create your tests here.
