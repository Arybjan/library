from django.db import models
from django.utils.translation import gettext_lazy as _


class ForumPost(models.Model):
    user = models.ForeignKey("", on_delete=models.CASCADE)
    topic = models.ForeignKey("", on_delete=models.CASCADE)
    title = models.CharField(_(""), max_length=240)
    body = models.TextField(_(""))
    created_at = models.DateTimeField(_(""))


class ForumTopic(models.Model):
    author = models.ForeignKey("", on_delete=models.CASCADE)
    name = models.CharField(_(""), max_length=200)
    created_at = models.DateTimeField(_(""))


class ForumPostReply(models.Model):
    user = models.ForeignKey("", on_delete=models.CASCADE)
    post = models.ForeignKey("", on_delete=models.CASCADE)
    body = models.TextField(_(""))
    created_at = models.DateTimeField(_(""))
    

