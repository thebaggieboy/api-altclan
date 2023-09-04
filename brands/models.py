from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from .display import LABEL_DISPLAY, COLLECTION_DISPLAY, COMMUNITY_TYPE_DISPLAY
from django.conf import settings
User = settings.AUTH_USER_MODEL
BrandUser = settings.BRAND_USER_MODEL
from .choices import STATUS, GENDER, COMMUNITY_TYPE

class Brand(models.Model):
    user = models.OneToOneField(BrandUser, on_delete=models.CASCADE, related_name='brand', null=True, blank=True)
    username = models.CharField(max_length=250)
    brand_name = models.CharField(max_length=250, default='')
    brand_logo = models.ImageField(upload_to='Brand Logos', default='')
    brand_bio = models.TextField(default='')
    brand_type = models.CharField(choices=COMMUNITY_TYPE, default='', max_length=250)
    date_created = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(null=True, blank=True, default='')

    def __str__(self):
        return f'{self.user} Brand'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.brand_name}')
        return super().save(*args, **kwargs)



class Merchandise(models.Model):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE,  null=True, blank=True)
    merchandise_name = models.CharField(max_length=250, default='')
    merchandise_color = models.CharField(max_length=250, default='')
    merchandise_size = models.CharField(max_length=250, default='')
    display_image = models.ImageField(upload_to='Merch Image', default='')
    labels = models.CharField(max_length=250, choices=LABEL_DISPLAY, default='')
    price = models.CharField(max_length=250, default='')
    delivery_cost = models.CharField(max_length=250, default='', null=True, blank=True)
    #images = models.ManyToManyField('MerchandiseGallery')
    slug = models.SlugField()

    date_created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'Merchandise Name : {self.merchandise_name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.brand} {self.merchandise_name} {self.merchandise_size} {self.merchandise_color}')
        return super().save(*args, **kwargs)

class MerchandiseGallery(models.Model):
    merchandise = models.OneToOneField(Merchandise, on_delete=models.CASCADE, related_name='merchandise_gallery', null=True, blank=True)
    image_1 = models.ImageField(upload_to='Merch Image', default='')
    image_2 = models.ImageField(upload_to='Merch Image', default='')
    image_3 = models.ImageField(upload_to='Merch Image', default='')
    image_4 = models.ImageField(upload_to='Merch Image', default='')
    image_5 = models.ImageField(upload_to='Merch Image', default='', null=True, blank=True)
    image_6 = models.ImageField(upload_to='Merch Image', default='', null=True, blank=True)

    def __str__(self):
        return f'Merchandise Name : {self.merchandise}'
 


class Leads(models.Model):
    brand_name = models.CharField(max_length=250, null=True, blank=True)
    instagram_username = models.CharField(max_length=250, null=True, blank=True)
    website_link = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, default='')
    def __str__(self):
        return f'Brands Leads'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.brand_name}')
        return super().save(*args, **kwargs)
# ProductOrder, these are the items that have been
class BillingAddress(models.Model):
    user = models.OneToOneField(BrandUser, on_delete=models.CASCADE, related_name='address', null=True, blank=True)
    street_address = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    zip = models.CharField(max_length=250, default='')

    def __str__(self):
        return f'{self.user}'
    
class UserBillingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_address', null=True, blank=True)
    street_address = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    zip = models.CharField(max_length=250, default='')

    def __str__(self):
        return f'{self.user}'    
# Inherits from brand

class Gallery(models.Model):
    pass

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    merchandises = models.ManyToManyField(Merchandise)
    address = models.ForeignKey('BillingAddress', on_delete=models.CASCADE, null=True, blank=True, )
    # Inherit order and bring it into the cart
    # Show list of orders and their quantities

    def __str__(self):
        return f'{self.merchandise} x ( {self.quantity} ) pcs by {self.user} '

# Represent a particular product order
class Order(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey('BillingAddress', on_delete=models.CASCADE)
    order_cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    order_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.user} has made an active order!'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=250, choices=STATUS, default='P')

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"