# Generated by Django 4.2.3 on 2023-08-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0005_remove_cart_name_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=123),
            preserve_default=False,
        ),
    ]
