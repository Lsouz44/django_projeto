# Generated by Django 5.0.4 on 2024-05-03 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_banner_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to='banner_imgs/'),
        ),
    ]
