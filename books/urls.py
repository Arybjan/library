from rest_framework.routers import DefaultRouter
from books import views

router = DefaultRouter()

router.register("book", views.BookViewSet)
router.register("tags", views.TagsViewSet)
router.register("book-tag", views.BookTagViewSet)
router.register("genre", views.GenreViewSet)
router.register("book-genre", views.BookGenreViewSet)
router.register("language", views.LanguageViewSet)
router.register("county-language", views.CountryLanguageViewSet)
router.register("favorite-books", views.FavoriteBooksViewSet)
router.register("format", views.FormatViewSet)
router.register("notes", views.NotesViewSet)
router.register("difficulty", views.DifficultyViewSet)
router.register("book-category", views.BookCategoryViewSet)
router.register("categories", views.CategoriesViewSet)

urlpatterns = router.urls
