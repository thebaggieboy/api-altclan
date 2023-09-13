from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Brand, Merchandise, Order, Cart, MerchandiseGallery, Leads
from django.conf import settings

BrandUser = settings.BRAND_USER_MODEL

from account.models import BrandProfile



class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand_name', 'brand_logo', 'brand_bio', 'slug']

class BrandProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandProfile
        fields = ['id','user','display_picture',  'mobile_number',  'email_address', 'merchandises',  'billing_address', 'city', 'state', 'zip']


class LeadsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = ['id','brand_name', 'instagram_username', 'website_link']



class MerchandiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchandise
        fields = [
            'id','brand', 'merchandise_name', 'merchandise_size', 'labels', 'delivery_cost', 'price'
        ]

class MerchandiseGallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MerchandiseGallery
        fields = [
            'id',
            'merchandise',
            'image_1',
            'image_2',
             'image_3',
             'image_4'
        ]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id','order_date', 'ordered', 'delivered', 'address']


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','quantity', 'merchandises']
