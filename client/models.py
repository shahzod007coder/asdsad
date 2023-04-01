from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField()


class Categoriya(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CategoriyaProduct(models.Model):
    categoriya = models.ForeignKey(Categoriya, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    categoriya = models.ForeignKey(Categoriya, null=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Product_min(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    brend = models.CharField(max_length=100)
    os_turi = models.CharField(max_length=100)
    ulchamlari = models.CharField(max_length=100)
    kamera = models.CharField(max_length=100)
    ol_kamera = models.CharField(max_length=100)
    korpus = models.CharField(max_length=100)
    ishlab_chiqarilgan_joyi = models.CharField(max_length=100)
    rang = models.CharField(max_length=100)
    yadrolar_son = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    xotira = models.CharField(max_length=100)
