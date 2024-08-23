
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('home',views.index,name='home'),
    path('products',views.list_products,name='product_list'),
    path('detail_product/<pk>',views.detail_product,name='detail_product'),
  


]
