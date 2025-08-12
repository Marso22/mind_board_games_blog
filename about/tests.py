from django.test import TestCase
from django.urls import reverse

class AboutPageTest(TestCase):
    """
    Test suite for the About page.
    """

    def test_about_page_loads(self):
        """
        Test that the About page loads successfully and contains the expected title.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Mind Board Games")
