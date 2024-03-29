# Generated by Django 4.2.9 on 2024-02-27 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('electronic', '0017_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='pincode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
