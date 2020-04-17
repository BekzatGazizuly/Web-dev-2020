from django.urls import path
from core.views import product_list
from core.views import product_detail
from core.views import category_list
from  core.views import category_details
from core.views import products_of_category
urlpatterns = [
path('products/', product_list),
path('products/<int:product_id>/', product_detail),
path('categories/', category_list),
path('categories/<int:category_id>/', category_details),
path('categories/<int:category_id>/products', products_of_category)
]