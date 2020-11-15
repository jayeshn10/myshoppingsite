from django.contrib import admin

# Register your models here.
from shop.models import Shopproduct, Category, Subcategory, Contactform

admin.site.register(Shopproduct)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Contactform)


