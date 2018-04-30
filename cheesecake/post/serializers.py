from rest_framework import serializers

from cheesecake.post.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'intro', 'post_url', 'category', 
                  'author_url', 'date')
        read_only_fields = ('id',)
