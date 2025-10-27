from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from users.models import User
from .serializers import UserSerializer

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Enviar notificación por email
            send_mail(
                'Nuevo Usuario Registrado',
                f'Se ha registrado un nuevo usuario:\n\n'
                f'Nombre: {user.name}\n'
                f'Email: {user.email}\n'
                f'Teléfono: {user.phone}',
                'from@example.com',
                ['admin@example.com'],
                fail_silently=False,
            )
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        