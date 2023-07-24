from django.urls import path
from .views import EventViewSet, UserList, UserDetail

app_name = 'church'

urlpatterns = [
    path('v1/users/', UserList.as_view(), name='userlist'),
    path('v1/user/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('v1/events/', EventViewSet.as_view({'get': 'list'}), name='event'),
]
