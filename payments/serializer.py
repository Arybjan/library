from rest_framework import serializers
from payments import models


class PremiumPurchase(serializers.ModelSerializer):
    class Meta:
        model = models.PremiumPurchase
        fields = "__all__"


class PaymentStatus(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentStatus
        fields = "__all__"
