from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import BrandProfile
from .models import Brand, Merchandise, MerchandiseGallery


# If a new brand is created, silmultaneously create a profile for the brand.


@receiver(post_save, sender=Merchandise)
def create_merchandise_profile(sender, instance, created, **kwargs):
    if created:
        MerchandiseGallery.objects.create(merchandise=instance)
        print("New Merch Gallery has been created")

@receiver(post_save, sender=Merchandise)
def save_merchandise_profile(sender, instance, **kwargs):
    instance.merchandise_gallery.save()
    print("Merchandise Gallery saved!")




