from django.contrib import admin

from products.models import Products

from products.models import Category

# Register your models here.
admin.site.register(Products)
admin.site.register(Category)