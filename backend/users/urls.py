from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('salud/', views.health_check, name='health-check'),
]