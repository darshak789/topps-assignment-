# views.py
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Product_mst, Product_sub_cat

class ProductManagerView(ListView):
    model = Product_mst
    template_name = 'products/product_manager.html'
    context_object_name = 'products'

class ProductSubCategoryDetailsView(DetailView):
    model = Product_mst
    template_name = 'products/product_sub_category_details.html'
    context_object_name = 'product'

    


