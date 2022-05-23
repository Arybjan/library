from rest_framework.routers import DefaultRouter
from forums import views

router = DefaultRouter()

router.register("post-reply", views.ForumPostReplyViewSet)
router.register("forum-post", views.ForumPostViewSet)
router.register("topic", views.ForumTopicViewSet)
router.register("marathon", views.MarathonsViewSet)
router.register("marathon-book", views.MarathonBooksViewSet)
router.register("marathon-user", views.MarathonUserViewSet)

urlpatterns = router.urls
