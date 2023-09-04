from django.contrib import admin
from .models import Brand, Merchandise, Cart, Order,  BillingAddress, MerchandiseGallery
from reviews.models import Reviews
# Register your models here.
from account.models import BrandProfile

class BrandInline(admin.TabularInline):
    model = Brand
    extra = 3

class BrandAdmin(admin.ModelAdmin):
    #inlines = [BrandInline]
    list_display = ['user', 'brand_name', 'brand_logo', 'brand_bio', 'date_created']
    list_filter = ['date_created']

class BrandProfileAdmin(admin.ModelAdmin):
    #inlines = [BrandInline]
    list_display = ['user', 'display_picture', 'email_address', 'slug']


class MerchandiseAdmin(admin.ModelAdmin):
    #inlines = [BrandInline]
    list_display = ['brand', 'merchandise_name', 'merchandise_color', 'merchandise_size', 'display_image', 'labels',  'price', 'delivery_cost', 'slug']

class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'city', 'state', 'zip']


class MerchandiseGalleryAdmin(admin.ModelAdmin):
    list_display = ['image_1', 'image_2', 'image_3', 'image_4',]

admin.site.register(BillingAddress, BillingAddressAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(BrandProfile, BrandProfileAdmin)
admin.site.register(Merchandise, MerchandiseAdmin)

admin.site.register(MerchandiseGallery, MerchandiseGalleryAdmin)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Reviews)




