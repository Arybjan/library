from rest_framework import serializers
from books import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = "__all__"


class BookTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = "__all__"


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookGenre
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = "__all__"


class CountryLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CountryLanguage
        fields = "__all__"


class FavoriteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteBooks
        fields = "__all__"


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Formats
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notes
        fields = "__all__"


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Difficulty
        fields = "__all__"


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = "__all__"
