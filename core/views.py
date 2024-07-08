
from django.http import JsonResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models.Product import Product

# Vista para la página principal
def home(request):
    return render(request, 'core/home.html')

# Vista para la lista de productos
'''def product_list(request, category_slug=None):
    category = None
    categories = TypeProduct.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(TypeProduct, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'core/products.html', {'category': category, 'categories': categories, 'products': products})

# Vista para el detalle del producto
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'core/product_detail.html', {'product': product})

# Vista para cerrar sesión
def exit(request):
    logout(request)
    return redirect('core:home')'''

@login_required
def products(request):
    products = Product.objects.all()
    return render(request, 'core/products.html', {'products': products})
#def products(request):
#    return render(request, 'core/products.html')



@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})

def exit(request):
    logout(request)
    return redirect('home')
