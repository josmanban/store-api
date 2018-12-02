from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import common.models as CommonModels
import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length = 500
        )
    description = models.TextField(blank= True, null = True)
    parent = models.ForeignKey(
        'Category',
        related_name = 'childs',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
        )
    
    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(
        User,
        related_name = 'productos',
        on_delete = models.SET_NULL,
        null = True
        )
    name = models.CharField(
        max_length = 500
        )
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        related_name = 'products',
        on_delete = models.SET_NULL,
        null = True
        )

    photo = models.ImageField(
        upload_to = 'products',
        null = True
        )

    price = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

   
class SaleState(CommonModels.State):
    pass

class Sale(models.Model):
    client =  models.ForeignKey(
        User,
        related_name = 'purchases',
        on_delete = models.SET_NULL,
        null = True
        )
    salesman = models.ForeignKey(
        User,
        related_name = 'sales',
        on_delete = models.SET_NULL,
        null = True
        )

    date = models.DateTimeField(default = timezone.now)

    state = models.ForeignKey(
        SaleState,
        related_name = 'sales',
        on_delete = models.SET_NULL,
        null = True
        )

    def get_total(self):
        total = 0
        for detail in self.details:
            total += detail.get_total
        return total


class SaleDetail(models.Model):
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    sale = models.ForeignKey(
        Sale,
        related_name="details",
        on_delete = models.SET_NULL,
        null = True
        )
    prouct = models.ForeignKey(
        Product,
        related_name="details",
        on_delete = models.SET_NULL,
        null = True
        )
    
    def get_total(self):
        return self.price*self.quantity