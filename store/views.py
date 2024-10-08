from itertools import product
from lib2to3.fixes.fix_input import context

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from carts.models import CartItem
from carts.views import _cart_id
from category.models import Category
from store.models import Product


# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else :
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug, is_available=True)
    in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
    context = {
        'single_product': product,
        'in_cart': in_cart
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
            context = {
                'products': products,
                'product_count': product_count
            }
            return render(request, 'store/store.html', context)
    return render(request, 'store/store.html')