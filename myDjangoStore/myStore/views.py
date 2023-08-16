from django.shortcuts import render

from myStore.models import Category, Product, Cart


def homePage(request):
    categories = Category.objects.all()
    products = Product.objects.filter(offerSale=True)
    cart = Cart.objects.first()

    return render(request,'myStore/home.html', {
        'title': 'Home | MyStore',
        'categories': categories,
        'products': products,
        'cart': cart,
    })


def categoryPage(request, id):
    categories = Category.objects.all()
    cart = Cart.objects.first()
    categorySelected = Category.objects.get(id=id)
    products = Product.objects.filter(categories=categorySelected)

    return render(request, 'myStore/category.html', {
        'title': 'Category | MyStore',
        'categories': categories,
        'products': products,
        'cart': cart,
        'categorySelected': categorySelected,
    })


def productsPage(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    cart = Cart.objects.first()
    return render(request,'myStore/products.html', {
        'title': 'Products | MyStore',
        'categories': categories,
        'products': products,
        'cart': cart,
    })

def productPage(request, id):
    categories = Category.objects.all()
    cart = Cart.objects.first()
    productSelected = Product.objects.get(id=id)
    products = Product.objects.all()

    return render(request,'myStore/product.html', {
        'title': 'Product | Products | MyStore',
        'categories': categories,
        'products': products,
        'cart': cart,
        'productSelected': productSelected,
    })

def cartPage(request):
    categories = Category.objects.all()
    cart = Cart.objects.first()
    products = Product.objects.all()

    return render(request,'myStore/cart.html', {
        'title': 'Cart | MyStore',
        'categories': categories,
        'products': products,
        'cart': cart,

    })
