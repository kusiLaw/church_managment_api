from django.urls import path, include
from .views import EventViewSet, UserViewSet, default_api_root
from rest_framework.routers import DefaultRouter

app_name = 'church'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
  path('',default_api_root),
  path('api/v1/',include((router.urls, 'church' ))),
]
