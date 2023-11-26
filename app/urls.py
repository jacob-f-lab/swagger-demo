#from django.urls import path, include
from rest_framework import routers
from .views import StickyNoteViewSet

router = routers.DefaultRouter()
router.register(r'sticky-note', StickyNoteViewSet)
urlpatterns = router.urls
