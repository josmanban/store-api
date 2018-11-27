from django.db import models

# Create your models here.

class Category(models.Model):
    name = None    
    class Meta:
        pass
    

class Product(models.Model):    
    name = None
    description = None
    category = None

    price = None

    is_active = None   


    def __init__(self):
        pass

    class Meta:
        pass

class Sale(models.Model):
    pass

class SaleDetail(models.Model):
    price = None
    numItems = None
    product = None
    pass

    class Meta:
        pass


