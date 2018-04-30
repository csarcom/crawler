from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from model_mommy import mommy


class BaseTests(APITestCase):

    @classmethod
    def setUpClass(cls):

        super(BaseTests, cls).setUpClass()

        cls.user = mommy.make(
            User,
            email="admin@admin.com",
            password="admin123",
            username="admin123")


def authenticate(function):
    def inner(self, *args, **kwargs):
        self.user = User.objects.get(email='admin@admin.com')
        token = Token.objects.create(user=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        return function(self, *args, **kwargs)

    return inner