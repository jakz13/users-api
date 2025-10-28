from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
import requests
import os

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Enviar notificación al microservicio
        user = serializer.instance
        notification_data = {
            'name': user.name,
            'email': user.email,
            'phone': user.phone
        }
        
        notification_url = os.getenv('NOTIFICATION_SERVICE_URL', 'http://notification-service:5000/notify')
        
        try:
            requests.post(notification_url, json=notification_data, timeout=5)
        except requests.exceptions.RequestException as e:
            # Log the error but don't fail the user creation
            print(f"Error enviando notificación: {e}")
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
