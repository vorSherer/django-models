from django.test import SimpleTestCase
from django.urls import reverse


class BlogTests(SimpleTestCase):

    def helper_page_status_200(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def helper_page_template_check(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, f'{url_name}.html')

    def test_home_page_status_pass(self):
        self.helper_page_status_200('home')

    def test_home_page_status_fail(self):
        response = self.client.get('fred')
        self.assertEqual(response.status_code, 404)

    def test_home_page_template(self):
        self.helper_page_template_check('home')

    def test_check_page_status(self):
        self.helper_page_status_200('check')

    def test_check_page_template(self):
        self.helper_page_template_check('check')
