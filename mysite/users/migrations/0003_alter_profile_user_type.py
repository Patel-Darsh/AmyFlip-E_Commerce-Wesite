# Generated by Django 4.2.9 on 2024-02-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('admin', 'admin'), ('com_owner', 'com_owner'), ('cust', 'cust')], max_length=100),
        ),
    ]
