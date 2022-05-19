from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(_(""), max_length=70)
    birthday_date = models.DateField(_("Дата рождения"))
    death_date = models.DateField(_("Дата смерти"))
    created_at = models.DateTimeField(_("Время создания"))


class FavoriteAuthors(models.Model):
    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    author = models.ForeignKey("authors.Author", on_delete=models.CASCADE)
    created_at = models.DateField(_("Время создания"))


class AuthorBook(models.Model):
    author = models.ForeignKey("authors.Author", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    licence_price = models.FloatField(_("Стоимость лицензии"))
    created_at = models.DateField(_("Время создания"))
