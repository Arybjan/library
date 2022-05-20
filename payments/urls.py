from rest_framework.routers import DefaultRouter
from payments import views

router = DefaultRouter()

router.register("premium-purchase", views.PremiumPurchaseViewSet)
router.register("payment-status", views.PaymentStatusViewSet)

urlpatterns = router.urls
