from django.urls import path
from . import views

app_name = 'church'

urlpatterns = [
    path('v1/users', views.users, name='users'),
    path('v1/user/<int:pk>/', views.user_detail, name='user_detail'),
]
