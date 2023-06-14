from django.urls import path
from ... import views

app_name = 'church'

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:id>/', views.user_detail, name='user_detail'),
]
