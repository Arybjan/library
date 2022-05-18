from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    full_name = models.CharField(_("ФИО"), max_length=250)
    username = models.CharField(_("Имя пользователя"), max_length=150)
    email = models.EmailField(_("Почта"), unique=True)
    birthday_date = models.DateField(_("День рождения"))
    gender = models.ForeignKey("users.Genders", on_delete=models.SET_NULL, null=True)
    occupation = models.ForeignKey("users.Occupations", on_delete=models.CASCADE)
    city = models.ForeignKey("users.Cities", on_delete=models.CASCADE)
    role = models.ForeignKey("users.Roles", on_delete=models.CASCADE)
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
    country = models.ForeignKey("users.Country", on_delete=models.CASCADE)


class Country(models.Model):
    name = models.CharField(_("Страна"), max_length=80)


class Occupations(models.Model):
    name = models.CharField(_("Занятость"), max_length=150)
