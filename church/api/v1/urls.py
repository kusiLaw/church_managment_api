from django.urls import path, include
from .views import EventViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'church'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('api/v1/',include((router.urls, 'church' ))),
]
