from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework import generics, views
from rest_framework.response import Response

from authorization.models import User
from authorization.serializers import LoginSerializer, RegistrationSerializer


# registration
class RegistrationView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)



# login
class LoginView(generics.GenericAPIView):

    queryset = User.objects.all()
    # serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"detail": "Logged in!"})
        return Response({"detail": "Error!"})


# logout
class LogoutView(generics.GenericAPIView):

    def get(self, request):
        logout(request)
        return Response({"detail": "Logged out!"})


# reset password
