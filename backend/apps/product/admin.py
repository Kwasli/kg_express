from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    list_display = ['name','slug','id']
    prepopulated_fields = {'slug':('name',)}



@admin.register(SubCategory)
class Subcategory(admin.ModelAdmin):
    list_display = ('name','category','slug','id')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('category',)
    search_fields = ('id','name')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'image',
        'category',
        'subcategory',
        'created',
        'updated',
        'is_active',

    ]