from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.site_header = "VEDInventory Dashboard"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category',)
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('product', 'staff', )
#     list_filter = ('product',)


admin.site.register(Order)
admin.site.register(ProductCategory)

# admin.site.unregister(Group)
