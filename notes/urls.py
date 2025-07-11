from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

# Use DRF DefaultRouter to automatically generate CRUD routes
router = DefaultRouter()
router.register("", NoteViewSet, basename="note")

urlpatterns = router.urls