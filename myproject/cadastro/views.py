from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

# Cadastro
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário cadastrado com sucesso"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login
class LoginAPIView(APIView):
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')

        # Tenta buscar por username ou por email
        user = User.objects.filter(username=login).first() or User.objects.filter(email=login).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login realizado com sucesso",
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_200_OK)

        return Response({"message": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST)