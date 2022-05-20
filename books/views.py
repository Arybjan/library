from rest_framework import viewsets
from books import models, serializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookSerializer


class TagsViewSet(viewsets.ModelViewSet):
    queryset = models.Tags.objects.all()
    serializer_class = serializer.TagsSerializer


class BookTagViewSet(viewsets.ModelViewSet):
    queryset = models.BookTag.objects.all()
    serializer_class = serializer.BookTagSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializer.GenreSerializer


class BookGenreViewSet(viewsets.ModelViewSet):
    queryset = models.BookGenre.objects.all()
    serializer_class = serializer.BookGenreSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = serializer.LanguageSerializer


class CountryLanguageViewSet(viewsets.ModelViewSet):
    queryset = models.CountryLanguage.objects.all()
    serializer_class = serializer.CountryLanguageSerializer


class FavoriteBooksViewSet(viewsets.ModelViewSet):
    queryset = models.FavoriteBooks.objects.all()
    serializer_class = serializer.FavoriteBookSerializer


class FormatViewSet(viewsets.ModelViewSet):
    queryset = models.Formats.objects.all()
    serializer_class = serializer.FormatSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = models.Notes.objects.all()
    serializer_class = serializer.NoteSerializer


class DifficultyViewSet(viewsets.ModelViewSet):
    queryset = models.Difficulty.objects.all()
    serializer_class = serializer.DifficultySerializer


class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.BookCategory.objects.all()
    serializer_class = serializer.BookCategorySerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = serializer.CategorySerializer
