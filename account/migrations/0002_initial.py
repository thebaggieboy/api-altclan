# Generated by Django 3.2.5 on 2023-10-04 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandprofile',
            name='merchandises',
            field=models.ManyToManyField(to='brands.Merchandise'),
        ),
        migrations.AddField(
            model_name='brandprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_profile', to='account.branduser'),
        ),
    ]
