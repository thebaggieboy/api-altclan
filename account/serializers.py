from rest_framework import serializers
from django.conf import settings
from .models import Profile, CustomUser

User = settings.AUTH_USER_MODEL
BrandUser = settings.BRAND_USER_MODEL
class BrandUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandUser
        fields = ['email', 'password']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'email_address', 'mobile_number', 'display_picture', 'country', 'street_address', 'city', 'state', 'zip']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
