# products/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', ProductManagerView.as_view(), name='product_manager'),
    path('admin/<int:pk>/', ProductSubCategoryDetailsView.as_view(), name='product_sub_category_details')
]
