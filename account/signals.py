
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Profile
from account.models import BrandUser
User = settings.AUTH_USER_MODEL
from account.models import BrandProfile, Brand
from brands.models import UserBillingAddress, BillingAddress

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        UserBillingAddress.objects.create(user=instance)
        print("New user profile has been created")

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.user_address.save()
    print("Profile saved!")
    print('User address saved')

# If a new brand is created, silmultaneously create a profile for the brand.
@receiver(post_save, sender=BrandUser)
def create_brand_profile(sender, instance, created, **kwargs):
    if created:
        BrandProfile.objects.create(user=instance)
        Brand.objects.create(user=instance)
        BillingAddress.objects.create(user=instance)
        print("New Brand Instance has been created")
        print("Brand Profile Created!")

@receiver(post_save, sender=BrandUser)
def save_brand_profile(sender, instance, **kwargs):
    instance.brand.save()
    instance.brand_profile.save()
    instance.address.save()
    print("Brand Profile saved!")
    print("Brand Address saved!")
   

