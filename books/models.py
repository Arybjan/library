from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(_("Название"), max_length=200)
    description = models.TextField(_("Описание"))
    release_date = models.DateField(_("Дата выпуска"))
    language = models.ForeignKey("books.Language", on_delete=models.CASCADE)
    format = models.ForeignKey("books.Formats", on_delete=models.CASCADE)
    words_num = models.IntegerField(_("Количество слов"))
    pages_num = models.IntegerField(_("Количество страниц"))
    is_premium = models.BooleanField(_("Премиум"))
    difficulty = models.ForeignKey("books.Difficulty", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Время создания"))


class Tags(models.Model):
    name = models.CharField(_("Теги"), max_length=190)


class BookTag(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    tag = models.ForeignKey("books.Tags", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Время создания"))


class Genre(models.Model):
    name = models.CharField(_("Жанр"), max_length=130)


class BookGenre(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    genre = models.ForeignKey("books.Genre", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Время создания"))


class Language(models.Model):
    name = models.CharField(_("Язык"), max_length=50)


class CountryLanguage(models.Model):
    country = models.ForeignKey("users.Country", on_delete=models.CASCADE)
    language = models.ForeignKey("books.Language", on_delete=models.CASCADE)


class FavoriteBooks(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Время создания"))


class Formats(models.Model):
    name = models.CharField(_("Формат"), max_length=20)


class Notes(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    book_id = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    page = models.IntegerField(_("Страница"))
    word_from = models.IntegerField(_("Слово от"))
    word_to = models.IntegerField(_("Слово для"))
    comment = models.TextField(_("Комментарий"))
    # parent_note = models.ForeignKey("books.Notes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Время создания"))


class Difficulty(models.Model):
    name = models.CharField(_("Сложность"), max_length=40)


class BookCategory(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    category = models.ForeignKey("books.Categories", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Время создания"))


class Categories(models.Model):
    name = models.CharField(_("Категория"), max_length=120)
