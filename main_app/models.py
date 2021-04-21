# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
            return f'{self.name}'

class City(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
            return f'{self.name}'

class Advert(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    city=models.ManyToManyField(City, blank=True)
    category=models.ManyToManyField(Category, blank=True)
    views=models.IntegerField(default=0)

    def __str__(self):
            return f'{self.title}'