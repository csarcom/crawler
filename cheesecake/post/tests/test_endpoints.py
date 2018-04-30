from django.urls import reverse
from rest_framework import status
from model_mommy import mommy

from cheesecake.base.tests import BaseTests, authenticate
from cheesecake.post.models import Post


class ViewPostTests(BaseTests):

    def test_permisions(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @authenticate
    def test_get_posts(self):

        mommy.make(Post)

        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
