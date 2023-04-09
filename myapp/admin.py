from django.contrib import admin
from .models import *
# Register your models here.


class Product_Images(admin.TabularInline):
    model = Product_Image


class Additional_Information(admin.TabularInline):
    model = Additional_Ingformation



class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Images,Additional_Information)
    list_display = ('product_name','categories','color','section')
    list_editable = ('categories','section','color')


class OrderItemTubleinline(admin.TabularInline):
    model = OrderItem



class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTubleinline]
    list_display = ['firstname','phone','email','payment_id','paid','date']
    search_fields = ['firstname','email','payment_id']


admin.site.register(slider)
admin.site.register(banner_area)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Section)
admin.site.register(Product, Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_Ingformation)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Coupon_Code)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)