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
