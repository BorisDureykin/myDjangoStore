# Generated by Django 4.2.3 on 2023-08-09 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0003_alter_product_countproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='myStore.category'),
        ),
    ]
