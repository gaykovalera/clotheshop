from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

User = get_user_model()
# TEST_USER = {
#     'email': 'test@test.com',
#     'password': '1234',
#     'password2': '1234',
# }

class TestRegistrationView(TestCase):

    def setUp(self):
        super().setUp()
        self.client = Client()
        self.url = reverse('authentication:registration')

    def test_registration_no_email(self):
        response = self.client.post(
            self.url, {'email': 'test@test.com', 'password1': '1234', 'password2': '1234'}
        )
        user = User.objects.get(email='test@test.com')



