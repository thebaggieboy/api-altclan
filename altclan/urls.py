
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from core.views import *
from account.views import BrandUserViewSet
from rest_framework_simplejwt import views as jwt_views
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'brand_users' , BrandUserViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'brand_profile', BrandProfileViewSet)
router.register(r'leads', LeadsViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'merchandises', MerchandiseViewSet)
router.register(r'merchandise_images', MerchandiseGalleryViewSet)
router.register(r'cart', CartViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    
    #path('api-auth/', include('dj_rest_auth.urls')),
    #path('api-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
  
  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   

