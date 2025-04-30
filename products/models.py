from django.db import models
from django.utils.timezone import datetime

class AuditData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField('Demo_User', null=False)
    class Meta:
        abstract = True

# Create your models here.
class Products(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalFiel(max_digits=10, decimal_places=2)
    isAvailable = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True,related_name='products')

class Category(AuditData):
    category_name = models.CharField(max_length=100,primary_key=True)
    category_description = models.TextField(blank=True)

