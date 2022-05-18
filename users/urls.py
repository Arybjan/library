from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()
router.register("users", views.UserViewSet)
router.register("role", views.RoleViewSet)
router.register("gender", views.GenderViewSet)
router.register("country", views.CountryViewSet)
router.register("occupation", views.OccupationViewSet)
router.register("city", views.CityViewSet)

urlpatterns = router.urls
