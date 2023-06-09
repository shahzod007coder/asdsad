# Generated by Django 4.1.3 on 2022-12-14 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('categoriya', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.categoriya')),
            ],
        ),
        migrations.CreateModel(
            name='Product_min',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brend', models.CharField(max_length=100)),
                ('os_turi', models.CharField(max_length=100)),
                ('ulchamlari', models.CharField(max_length=100)),
                ('kamera', models.CharField(max_length=100)),
                ('ol_kamera', models.CharField(max_length=100)),
                ('korpus', models.CharField(max_length=100)),
                ('ishlab_chiqarilgan_joyi', models.CharField(max_length=100)),
                ('rang', models.CharField(max_length=100)),
                ('yadrolar_son', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
                ('xotira', models.CharField(max_length=100)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]
