# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50, primary_key=True)

    def __str__(self):
            return f'{self.name}'


class City(models.Model):
    name=models.CharField(max_length=50, primary_key=True)

    def __str__(self):
            return f'{self.name}'
            

class Advert(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    city=models.ManyToManyField(City, blank=True, related_name='adverts')
    category=models.ManyToManyField(Category, blank=True, related_name='adverts')
    views=models.IntegerField(default=0)

    def __str__(self):
            return f'{self.title}'