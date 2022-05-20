from rest_framework import viewsets
from payments import models, serializer


class PremiumPurchaseViewSet(viewsets.ModelViewSet):
    queryset = models.PremiumPurchase.objects.all()
    serializer_class = serializer.PremiumPurchaseSerializer


class PaymentStatusViewSet(viewsets.ModelViewSet):
    queryset = models.PaymentStatus.objects.all()
    serializer_class = serializer.PremiumPurchaseSerializer
