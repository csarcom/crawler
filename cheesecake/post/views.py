from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from cheesecake.post.serializers import PostSerializer
from cheesecake.post.models import Post


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
