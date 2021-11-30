from http import HTTPStatus
from urllib.parse import urlparse, parse_qsl

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse, resolve

from apps.cart.cart import Cart
from apps.catalog.models import Brand, Category, Product

User = get_user_model()

TEST_USER = {
    'email': 'test@test.com',
    'password': '1234'
}


class TestCartCases(TestCase):

    def setUp(self):
        super().setUp()
        # self.user = User.objects.create(email=TEST_USER['email'], password=TEST_USER['password'])
        # self.cart = Cart.objects.create(owner=self.user)
        self.client = Client()


    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.base_url = 'cart:cart_add'

    def test_cart_redirect(self):
        client = Client
        url = reverse(
            'cart:cart_add',
            kwargs={'/cart/'}
        )

        response = self.client.get(url)

        parsed_url = urlparse(response.url)
        query_dict: dict = dict(parse_qsl(parsed_url.query))
        redirect_url = resolve(parsed_url.path)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(redirect_url.url_name, 'authentication:login')
        self.assertEqual(query_dict['next'], url)



