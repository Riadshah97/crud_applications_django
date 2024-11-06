# admin.py
from django.contrib import admin
from .models import User, Product

class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email')  # Display these fields in the admin list view
    search_fields = ('username', 'email' 'password')  

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price')  # Display fields in list view
    search_fields = ('name', 'description', 'price', 'user') 

# Register the models with the admin
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
