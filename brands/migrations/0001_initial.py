# Generated by Django 3.2.5 on 2023-10-04 07:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('street_address', models.CharField(default='', max_length=250)),
                ('city', models.CharField(default='', max_length=250)),
                ('state', models.CharField(default='', max_length=250)),
                ('zip', models.CharField(default='', max_length=250)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='account.branduser')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=250)),
                ('brand_name', models.CharField(default='', max_length=250)),
                ('brand_logo', models.ImageField(default='', upload_to='Brand Logos')),
                ('brand_bio', models.TextField(default='')),
                ('brand_type', models.CharField(choices=[('Clothing and Apparel', 'Clothing and Apparel'), ('Accessories', 'Accessories'), ('Arts', 'Arts'), ('Footwears & Canvas', 'Footwears & Canvas')], default='', max_length=250)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2023, 10, 4, 7, 12, 14, 224439, tzinfo=utc))),
                ('slug', models.SlugField(blank=True, default='', null=True, unique=True)),
                ('followers', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='account.branduser')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.billingaddress')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('brand_name', models.CharField(blank=True, max_length=250, null=True)),
                ('instagram_username', models.CharField(blank=True, max_length=250, null=True)),
                ('website_link', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('merchandise_name', models.CharField(default='', max_length=250)),
                ('merchandise_color', models.CharField(default='', max_length=250)),
                ('merchandise_size', models.CharField(default='', max_length=250)),
                ('display_image', models.ImageField(default='', upload_to='Merch Image')),
                ('labels', models.CharField(choices=[('None', 'None'), ('New Merchandise', 'New Merchandise'), ('Limited Stock', 'Limited Stock'), ('FREE DELIVERY', 'FREE DELIVERY')], default='', max_length=250)),
                ('price', models.CharField(default='', max_length=250)),
                ('delivery_cost', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('slug', models.SlugField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2023, 10, 4, 7, 12, 14, 224439, tzinfo=utc))),
                ('brand', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ordered', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('order_date', models.DateTimeField(default=datetime.datetime(2023, 10, 4, 7, 12, 14, 229447, tzinfo=utc))),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.billingaddress')),
                ('order_cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.cart')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserBillingAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('street_address', models.CharField(default='', max_length=250)),
                ('city', models.CharField(default='', max_length=250)),
                ('state', models.CharField(default='', max_length=250)),
                ('zip', models.CharField(default='', max_length=250)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Completed'), ('F', 'Failed')], default='P', max_length=250)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MerchandiseGallery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image_1', models.ImageField(default='', upload_to='Merch Image')),
                ('image_2', models.ImageField(default='', upload_to='Merch Image')),
                ('image_3', models.ImageField(default='', upload_to='Merch Image')),
                ('image_4', models.ImageField(default='', upload_to='Merch Image')),
                ('image_5', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('image_6', models.ImageField(blank=True, default='', null=True, upload_to='Merch Image')),
                ('merchandise', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='merchandise_gallery', to='brands.merchandise')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='merchandises',
            field=models.ManyToManyField(to='brands.Merchandise'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
