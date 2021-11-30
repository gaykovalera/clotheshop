from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from apps.catalog.models import Brand, Category
from .fixtures.brand import TEST_BRAND, TEST_CATEGORY

User = get_user_model()

TEST_USER = {
    'email': 'test@test.com',
    'password': '1234'
}


class TestBrandView(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        user_obj = User(email=TEST_USER['email'])
        user_obj.set_password(TEST_USER['password'])
        user_obj.save()
        cls.user = user_obj

        cls.client = Client()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.base_url = 'catalog:brand_view'

    def setUp(self):
        super().setUp()
        self.client = Client()

    def test_brand_view_not_found(self):
        self.client.login(email=self.user.email, password=TEST_USER['password'])
        url = reverse(
            self.base_url,
            kwargs={'brand_slug': 'test'}
                      )

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_brand_view_ok(self):
        self.client.login(email=self.user.email, password=TEST_USER['password'])

        Brand.objects.create(**TEST_BRAND)
        url = reverse(
            self.base_url,
            kwargs={'brand_slug': TEST_BRAND['slug']}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.templates[0].name, 'catalog/brand.html')
        self.assertEqual(response.context['brand'].slug, TEST_BRAND['slug'])












