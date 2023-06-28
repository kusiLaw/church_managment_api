from django.urls import path
from .views import EventsList, UsersList

app_name = 'church'

urlpatterns = [
    path('v1/users', UsersList.as_view(), name='users'),
    path('v1/user/<int:pk>/', views.user_detail, name='user_detail'),
    path('v1/events/', EventsList.as_view(), name='event'),
]
