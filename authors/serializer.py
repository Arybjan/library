from rest_framework import serializers
from authors import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"


class FavoriteAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.FavoriteAuthors
        fields = "__all__"


class AuthorBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthorBook
        fields = "__all__"
