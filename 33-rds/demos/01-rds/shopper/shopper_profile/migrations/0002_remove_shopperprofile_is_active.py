# Generated by Django 2.0.4 on 2018-04-25 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopper_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopperprofile',
            name='is_active',
        ),
    ]