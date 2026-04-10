from django.urls import path
from .views import *
urlpatterns = [
    path("products-list/", ProductListView.as_view(), name="products_list"),
    path("product-create/", ProductCreateView.as_view(), name="product_create"),
    path("product-detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product-update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product-delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
    