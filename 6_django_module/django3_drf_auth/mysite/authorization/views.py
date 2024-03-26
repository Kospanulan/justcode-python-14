from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from rest_framework.response import Response

from authorization.models import User
from authorization.serializers import LoginSerializer


# registration


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
