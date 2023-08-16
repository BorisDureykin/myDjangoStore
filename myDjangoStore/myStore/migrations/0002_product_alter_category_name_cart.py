# Generated by Django 4.2.3 on 2023-08-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128)),
                ('description', models.TextField(max_length=1024)),
                ('countProduct', models.IntegerField(max_length=32)),
                ('slug', models.SlugField(max_length=64)),
                ('status', models.BooleanField(default=True)),
                ('offerSale', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(db_index=True, max_length=1024),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('products', models.ManyToManyField(to='myStore.product')),
            ],
        ),
    ]
