from django.contrib import admin

# Register your models here.

from .models import Advert, City, Category

class AdvertAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'city', 'category', 'views']

admin.site.register(Advert, AdvertAdmin)

class CityAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(City, CityAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    
admin.site.register(Category, CategoryAdmin)