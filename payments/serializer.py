from rest_framework import serializers
from payments import models


class PremiumPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PremiumPurchase
        fields = "__all__"


class PaymentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentStatus
        fields = "__all__"
