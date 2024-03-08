# Generated by Django 4.2.9 on 2024-02-27 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('electronic', '0016_delete_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='address', max_length=300)),
                ('city', models.CharField(default='city', max_length=300)),
                ('state', models.CharField(default='state', max_length=300)),
                ('country', models.CharField(default='India', max_length=300)),
                ('pincode', models.IntegerField(default='000001')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
