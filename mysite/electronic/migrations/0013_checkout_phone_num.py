# Generated by Django 4.2.9 on 2024-02-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0012_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='phone_num',
            field=models.CharField(default=91, max_length=10),
        ),
    ]
