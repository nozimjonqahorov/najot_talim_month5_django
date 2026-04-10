from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from .forms import CategoryForm, ProductForm
from django.views import View
from django.contrib import messages
from django.db.models import Q

from config.mixins import MyLoginRequiredMixin
    

class ProductListView(View):
    def get(self, request):
        query = request.GET.get("q")
        cat_id = request.GET.get("category") 
        my_products = request.GET.get("my_products") # URL'dan 'my_products' parametrini tekshiramiz (masalan: ?my_products=true)
        
        categories = Category.objects.all()
        products = Product.objects.filter(is_available=True)

        if my_products == 'true' and request.user.is_authenticated:
            products = products.filter(seller=request.user)

        if cat_id:
            products = products.filter(category_id=cat_id)

        if query:
            products = products.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
  
        return render(request, "shop/products_list.html", {"products": products, "categories": categories})


class ProductCreateView(MyLoginRequiredMixin, View):
    def get(self, request):
        form = ProductForm()
        return render(request, "shop/product_create.html", {"form":form})
    
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False) # Bazaga yozishni vaqtincha to'xtatamiz Modelda seller bor lekin formada yuq.
            product.seller = request.user     # Hozirgi foydalanuvchini biriktiramiz. Mahsulot yaratgan user ushbu produktani selleri buladi.
            product.save()                    # Endi saqlaymiz
            return redirect("products_list")
        return render(request, "shop/product_create.html", {"form":form})
    

class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk = pk)
        return render(request, "shop/product_detail.html", {"product":product})
    

class ProductUpdateView(MyLoginRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        
        # Sotuvchini tekshiramiz
        if product.seller != request.user:
            messages.error(request, "Kechirasiz, bu mahsulot sizniki emas! Uni tahrirlash huquqingiz yo'q.")
            # Detail sahifasiga qaytaramiz
            return redirect("product_detail", pk)
        
        form = ProductForm(instance=product)
        return render(request, "shop/product_update.html", {"form": form, "product": product})
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk = pk)
        form =ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            if product.seller == request.user:
                product.save()
                return redirect("product_detail", pk)
            messages.error(request, "Kechirasiz, bu mahsulot sizniki emas! Uni tahrirlash huquqingiz yo'q.")
            return redirect("product_detail", pk)
        return render(request, "shop/product_update.html", {"form":form, "product":product})

            
class ProductDeleteView(MyLoginRequiredMixin, View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.seller != request.user:
            messages.error(request, "Kechirasiz, bu mahsulot sizniki emas! Uni o'chirish huquqingiz yo'q.")
            return redirect("product_detail", pk)
        return render(request, "shop/product_delete.html", {"product":product})
    
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.seller != request.user:
            messages.error(request, "Kechirasiz, bu mahsulot sizniki emas! Uni tahrirlash huquqingiz yo'q.")
            return redirect("product_detail", pk)
        product.delete()
        return redirect("products_list")
