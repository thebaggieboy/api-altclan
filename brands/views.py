from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from account.models import BrandProfile
from .models import Brand, Order, Cart, Merchandise, MerchandiseGallery, Leads
from .serializers import(
      OrderSerializer,
      CartSerializer,
      LeadsSerializer,
      MerchandiseSerializer,
      BrandProfileSerializer,
      BrandSerializer,
      BrandUserSerializer,
      MerchandiseGallerySerializer
)

class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer

class MerchandiseGalleryViewSet(viewsets.ModelViewSet):
    queryset = MerchandiseGallery.objects.all()
    serializer_class = MerchandiseGallerySerializer

class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Create your views here.
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

# Create your views here.
class BrandProfileViewSet(viewsets.ModelViewSet):
    queryset = BrandProfile.objects.all()
    serializer_class = BrandProfileSerializer




def create_merchandise_list(request):

    return render(request, 'alteclan/index.html')