from django.db import models
from django.utils.translation import gettext_lazy as _


class ForumPost(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    topic = models.ForeignKey("forums.ForumTopic", on_delete=models.CASCADE)
    title = models.CharField(_("Заголовок"), max_length=240)
    body = models.TextField(_("Описание"))
    created_at = models.DateTimeField(_("Время создания"))


class ForumTopic(models.Model):
    author = models.ForeignKey("authors.Author", on_delete=models.CASCADE)
    name = models.CharField(_("Наименование"), max_length=200)
    created_at = models.DateTimeField(_("Время создания"))


class ForumPostReply(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("forums.ForumPost", on_delete=models.CASCADE)
    body = models.TextField(_("Описание"))
    created_at = models.DateTimeField(_("Время создания"))


class Marathons(models.Model):
    title = models.CharField(_("Заголовок"), max_length=240)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    date_from = models.DateField(_("Дата начала"))
    date_to = models.DateField(_("Дата конца"))
    created_at = models.DateTimeField(_("Время создания"))


class MarathonBooks(models.Model):
    marathon = models.ForeignKey("forums.Marathons", on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)


class MarathonUsers(models.Model):
    marathon = models.ForeignKey("forums.Marathons", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
