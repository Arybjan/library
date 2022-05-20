from rest_framework import viewsets
from authors import models
from authors.serializer import (
    AuthorSerializer,
    AuthorBookSerializer,
    FavoriteAuthorsSerializer
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorBookViewSet(viewsets.ModelViewSet):
    queryset = models.AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer


class FavoriteAuthors(viewsets.ModelViewSet):
    queryset = models.FavoriteAuthors.objects.all()
    serializer_class = FavoriteAuthorsSerializer
