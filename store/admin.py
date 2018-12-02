from django.contrib import admin

from store.models import *

# Register your models here.

#admin.site.register(Category)
admin.site.register(SaleState)
#@admin.register(SaleDetail)
#class SaleDetailAdmin(admin.ModelAdmin):
#    pass
#

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display=('name','description','parent')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','price','user','is_active')

class SaleDetailInline(admin.TabularInline):
    model = SaleDetail   

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    inlines = (SaleDetailInline,)