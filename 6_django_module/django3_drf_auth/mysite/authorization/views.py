from django.contrib.auth.hashers import make_password
from rest_framework import generics

from authorization.models import User
from authorization.serializers import RegistrationSerializer


# registration
class RegistrationView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)


