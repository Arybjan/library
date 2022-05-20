from django.db import models
from django.utils.translation import gettext_lazy as _


class PremiumPurchase(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    payment_amount = models.FloatField(_("Сумма платежа"))
    status = models.ForeignKey("payments.PaymentStatus", on_delete=models.CASCADE)
    date_from = models.DateTimeField(_("Дата начала"))
    date_to = models.DateTimeField(_("Дата конца"))
    created_at = models.DateTimeField(_("Время создания"))


class PaymentStatus(models.Model):
    name = models.CharField(_("Статус"), max_length=100)
