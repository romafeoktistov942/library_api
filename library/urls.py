from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, BookIssueViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"bookissues", BookIssueViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
