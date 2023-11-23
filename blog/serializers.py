from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Post, Tag

# region post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['full_name']
        read_only_fields = fields


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = fields


class ContentSerializer(serializers.Serializer):
    plain = serializers.CharField()
    html = serializers.CharField()
    delta = serializers.CharField()

    class Meta:
        fields = ['plain', 'html', 'delta']
        read_only_fields = fields


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    content = ContentSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = [f.name for f in Post._meta.get_fields()]


# endregion

# region tag


class TagWithPostsSerializer(serializers.ModelSerializer):
    posts: serializers.PrimaryKeyRelatedField = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'posts']
        read_only_fields = fields


# endregion
