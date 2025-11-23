from .views import BlogListViewSet
# from apps.blog.views import BlogListView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"", BlogListViewSet, basename="blog")

urlpatterns = router.urls
