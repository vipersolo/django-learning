from django.contrib import admin
from .models import Product,Category
# Register your models here.




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    search_fields = ("name",)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","category","price")
    search_fields = ("name","category__name")
    list_filter = ("category",)
    list_per_page = 25
    autocomplete_fields = ("category",)
    list_select_related = ("category",) # to use sql join(single query instead of 2 ) , solves n+1 query , ie extra query to turn category id to name etc...