from .models import Category, City, Advert
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class AdvertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advert
        # fields = ['title', 'description', 'city', 'category', 'views']
        fields = ['title', 'description', 'views']