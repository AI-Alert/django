from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CommentViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='user')
router.register(r'comment', CommentViewSet, basename='user')
router.register(r'category', CategoryViewSet, basename='user')

urlpatterns = router.urls