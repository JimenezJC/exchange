from django.contrib import admin

from .models import *

# admin.site.register(Brand)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields= {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)
# admin.site.register(SubCatergory)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category', 'price', 'seller', 'stock','available', 'created','updated']
    list_filter = ['available', 'created', 'seller', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
# admin.site.register(Listing)