# Generated by Django 5.0.4 on 2024-05-03 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_banner_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_feat_caracterico',
            new_name='produto_em_destaque',
        ),
    ]
