from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    full_name = models.CharField(_('ФИО'), max_length=250)
    username = models.CharField(max_length=150)
    email = models.EmailField(_("Почта"), unique=True)
    birthday_date = models.DateField()
    gender_id = models.ForeignKey("users.Genders", on_delete=models.SET_NULL, null=True)
    occupation_id = models.ForeignKey("", on_delete=models.CASCADE)
    city_id = models.ForeignKey("", on_delete=models.CASCADE)
    role_id = models.ForeignKey("", on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.full_name


class Genders(models.Model):
    name = models.CharField(_("Пол"), max_length=100)


class Roles(models.Model):
    name = models.CharField(_("Роль"), max_length=150)


class Cities(models.Model):
    name = models.CharField(_("Город"), max_length=100)
    country_id = models.ForeignKey("users.Counrty", on_delete=models.CASCADE)


class Country(models.Model):
    name = models.CharField(_("Страна"), max_length=80)


class Occupations(models.Model):
    name = models.CharField(_("Занятость"), max_length=150)
