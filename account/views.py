
from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer, BrandUserSerializer
from .models import Profile, CustomUser, BrandUser

from django.conf import settings
#BrandUser = settings.BRAND_USER_MODEL


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class BrandUserViewSet(viewsets.ModelViewSet):
    queryset = BrandUser.objects.all()
    serializer_class = BrandUserSerializer
