from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Brand, Merchandise, Order, Cart, MerchandiseGallery, Leads
from django.conf import settings

BrandUser = settings.BRAND_USER_MODEL

from account.models import BrandProfile



class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_name', 'brand_logo', 'brand_bio']

class BrandProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandProfile
        fields = ['brand','display_picture',  'mobile_number',  'email_address', 'merchandises', 'country', 'street_address', 'city', 'state', 'zip']


class LeadsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = ['brand_name', 'instagram_username', 'website_link']



class MerchandiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchandise
        fields = [
            'brand', 'merchandise_name', 'merchandise_size', 'labels', 'delivery_cost', 'price'
        ]

class MerchandiseGallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MerchandiseGallery
        fields = [
            'merchandise',
            'image_1',
            'image_2',
             'image_3',
             'image_4'
        ]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['order_date', 'ordered', 'delivered', 'address']


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity', 'merchandises']
