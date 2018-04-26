# Generated by Django 2.0.4 on 2018-04-26 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_auto_20180426_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='published',
            field=models.CharField(choices=[('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public')], max_length=250),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(default='Untitled', max_length=250),
        ),
        migrations.AlterField(
            model_name='photo',
            name='published',
            field=models.CharField(choices=[('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public')], max_length=250),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(default='Untitled', max_length=250),
        ),
    ]
