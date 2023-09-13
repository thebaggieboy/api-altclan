from rest_framework import serializers
from django.conf import settings
from .models import Profile, CustomUser, BrandUser


class BrandUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandUser
        fields = ['id', 'email', 'password', 'token']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user', 'first_name', 'last_name', 'email_address', 'mobile_number', 'display_picture', 'billing_address', 'city', 'state', 'zip']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email', 'password', 'token']
