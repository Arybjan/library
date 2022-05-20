from rest_framework.routers import DefaultRouter
from authors import views

router = DefaultRouter()

router.register("author", views.AuthorViewSet)
router.register("author-book", views.AuthorBookViewSet)
router.register("favorite-author", views.FavoriteAuthorsViewSet)

urlpatterns = router.urls
