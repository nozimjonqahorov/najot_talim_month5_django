from .models import Category, Product
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "title", "description", "price", "photo", "is_available"]
