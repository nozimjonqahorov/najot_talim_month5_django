from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # Nomdan slug yasaydi

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_available', 'seller', 'created_at'] # Ro'yxatda ko'rinadigan ustunlar
    list_filter = ['is_available', 'category'] # Filtrlash oynasi
    search_fields = ['title', 'description'] # Qidiruv maydoni