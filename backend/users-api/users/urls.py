from django.urls import path
from .views_modified import UserListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
]
