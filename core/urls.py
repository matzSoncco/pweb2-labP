from django.urls import path
from . import views
from .views import home, products, exit
from .views import products, product_detail

urlpatterns = [
    #path('', views.home, name='home'),
    #path('productos/', views.product_list, name='product_list'),
    #path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    #path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    #path('salir/', views.exit, name='exit'),
    path('', home, name='home'),
    path('core/products/', products, name='products'),
    path('core/products/<int:product_id>/', product_detail, name='product_detail'),
    path('logout/', exit, name='exit'),
]