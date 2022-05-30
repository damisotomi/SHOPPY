from django.contrib import admin

# Register your models here.
#because you want to control your model in the admin app, you register it here.
#you create a modeladmin class for your models and register them because you want
#to configure the things that are listed in the admin interface


from products.models import Product
from products.models import Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)